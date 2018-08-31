import pyopencl as cl
import numpy as np
import os
from essentials import program, ctx, queue
from gtypes import gtype, is_gtype_valid, map_type

_script_dir = os.path.split(os.path.realpath(__file__))[0]

_dtype_mapping = ((np.float64, np.float32), (np.int64, np.int32))
_dtype_mapping = tuple(map(lambda x: tuple(map(lambda y: gtype(y), x)), _dtype_mapping))
_dtype_disabled = tuple(map(lambda x: x[0], _dtype_mapping))

_prg = program(os.path.join(_script_dir, "mat.cl"))

class Mat:
    @property
    def shape(self):
        return self._shape
    @property
    def dtype(self):
        return self._dtype
    @property
    def gtype(self):
        return self._dtype
    
    def __init__(self, shape=None, dtype=None, init=None):
        if not dtype is None and not is_gtype_valid(dtype):
            raise ValueError("Type %s is not allowed" % str(gtype(dtype)))
        if init is None:
            hostbuf = None
        else:
            hostbuf = np.array(init)
            for _dtype_mapping_item in _dtype_mapping:
                if hostbuf.dtype == _dtype_mapping_item[0]:
                    hostbuf = hostbuf.astype(_dtype_mapping_item[1])
        if hostbuf is None:
            self._shape = shape or tuple()
            self._dtype = gtype(dtype)
            hostbuf = np.empty(self._shape, dtype=self._dtype)
        if len(hostbuf.shape) == 0:
            self._shape = shape or tuple()
            self._dtype = gtype(dtype or hostbuf.dtype)
            hostbuf = np.zeros(self._shape, dtype=self._dtype) + hostbuf.astype(self._dtype)
        else:
            self._shape = hostbuf.shape
            self._dtype = gtype(dtype or hostbuf.dtype)
            hostbuf = hostbuf.astype(self._dtype)
        self.buffer = cl.Buffer(ctx, cl.mem_flags.READ_WRITE | cl.mem_flags.COPY_HOST_PTR, hostbuf=hostbuf)

    def gather(self):
        hostbuf = np.empty(self._shape, dtype=self._dtype)
        cl.enqueue_copy(queue, hostbuf, self.buffer)
        return hostbuf

    def _check_other_and_get_op(va, vb, base_op):
        ismat_a = isinstance(va, Mat)
        ismat_b = isinstance(vb, Mat)
        pytype_a = map_type(va.dtype).type if ismat_a else type(va)
        pytype_b = map_type(vb.dtype).type if ismat_b else type(vb)
        pytype_a_str = str(pytype_a).replace("<class '", "").replace("'>", "")
        pytype_b_str = str(pytype_b).replace("<class '", "").replace("'>", "")
        if ismat_a and ismat_b:
            if va.shape != vb.shape:
                raise ValueError("Matrix dimensions or shapes not match")
            elif va.dtype != vb.dtype:
                raise ValueError("Matrix types not match")
            else:
                return base_op[va.dtype].kernel_base
        elif ismat_a and not ismat_b:
            if not pytype_a == pytype_b:
                raise ValueError("Left matrix with type '%s' is not competible with right scalar with type '%s'" % (str(va.dtype), pytype_b_str))
            else:
                return base_op[va.dtype].kernel_scalar
        elif not ismat_a and ismat_b:
            if not pytype_a == pytype_b:
                raise ValueError("Left scalar with type '%s' is not competible with right matrix with type '%s'" % (pytype_a_str, str(vb.dtype)))
            else:
                return base_op[va.dtype].kernel_byscalar
        else:
            raise ValueError("Neither is a matrix")
            return base_op[va.dtype]



    def __add__(self, other):
        _check_other_and_get_op(other)


