import numpy as np

class gtype(np.dtype):
    pass

float32 = gtype(np.float32)
int32 = gtype(np.int32)
int8 = gtype(np.int8)
uint32 = gtype(np.uint32)
uint8 = gtype(np.uint8)

_modgpu_supported_dtype_gputype_mapping = [
    (float32, "float"),
    (int32, "int"),
    (int8, "char"),
    (uint32, "unsigned int"),
    (uint8, "unsigned char"),
]
_modgpu_supported_dtypes = list(map(lambda x: x[0], _supported_dtype_mapping))

def is_gtype_valid(the_dtype):
    if not isinstance(the_dtype, np.dtype):
        return False
    return the_dtype in _modgpu_supported_dtypes
