import pyopencl as cl
import numpy as np
import os
from essentials import program, ctx, queue

_script_dir = os.path.split(os.path.realpath(__file__))[0]

_dtype_mapping = ((np.float64, np.float32), (np.int64, np.int32))
_dtype_mapping = tuple(map(lambda x: tuple(map(lambda y: np.dtype(y), x)), _dtype_mapping))
_dtype_disabled = tuple(map(lambda x: x[0], _dtype_mapping))

_prg = program(os.path.join(_script_dir, "mat.cl"))

class Mat:
    def __init__(self, shape=None, dtype=None, init=None):
        if not dtype is None and np.dtype(dtype) in _dtype_disabled:
            raise ValueError("Type %s is not allowed" % str(np.dtype(dtype)))
        if init is None:
            hostbuf = None
        else:
            hostbuf = np.array(init)
            for _dtype_mapping_item in _dtype_mapping:
                if hostbuf.dtype == _dtype_mapping_item[0]:
                    hostbuf = hostbuf.astype(_dtype_mapping_item[1])
        if hostbuf is None:
            self.shape = shape or tuple()
            self.dtype = np.dtype(dtype)
            hostbuf = np.empty(self.shape, dtype=self.dtype)
        if len(hostbuf.shape) == 0:
            self.shape = shape or tuple()
            self.dtype = np.dtype(dtype or hostbuf.dtype)
            hostbuf = np.zeros(self.shape, dtype=self.dtype) + hostbuf.astype(self.dtype)
        else:
            self.shape = hostbuf.shape
            self.dtype = np.dtype(dtype or hostbuf.dtype)
            hostbuf = hostbuf.astype(self.dtype)
        self.buffer = cl.Buffer(ctx, cl.mem_flags.READ_WRITE | cl.mem_flags.COPY_HOST_PTR, hostbuf=hostbuf)

    def gather(self):
        hostbuf = np.empty(self.shape, dtype=self.dtype)
        cl.enqueue_copy(queue, hostbuf, self.buffer)
        return hostbuf

    def __add__(self, other):
        if isinstance(other, Mat):

