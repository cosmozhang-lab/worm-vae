import numpy as np

class gtype(np.dtype):
    pass

float32 = gtype(np.float32)
int32 = gtype(np.int32)
int8 = gtype(np.int8)
uint32 = gtype(np.uint32)
uint8 = gtype(np.uint8)

class _modgpu_supported_dtype_mapping_item:
    def __init__(self, _name, _gtype, _dtype, _gputype, _pytype):
        self.name = _name
        self.gtype = _gtype
        self.dtype = _dtype
        self.gputype = _gputype
        self.type = _pytype

_modgpu_supported_dtype_gputype_mappings = [
    _modgpu_supported_dtype_mapping_item("float32", float32, np.float32, "float",         float),
    _modgpu_supported_dtype_mapping_item("int32",   int32,   np.int32,   "int",           int),
    _modgpu_supported_dtype_mapping_item("int8",    int8,    np.int8,    "char",          int),
    _modgpu_supported_dtype_mapping_item("uint32",  uint32,  np.uint32,  "unsigned int",  int),
    _modgpu_supported_dtype_mapping_item("uint8",   uint8,   np.uint8,   "unsigned char", int)
]
_modgpu_supported_dtypes = list(map(lambda x: x.gtype, _modgpu_supported_dtype_gputype_mappings))

def map_type(given):
    if isinstance(given, gtype):
        attrname = "gtype"
    elif isinstance(given, np.dtype):
        attrname = "dtype"
    elif isinstance(given, str):
        attrname = "gputype"
    elif isinstance(given, float):
        attrname = "type"
    elif isinstance(given, int):
        attrname = "type"
    else:
        raise ValueError("Not recognized given value type")
    for item in _modgpu_supported_dtype_gputype_mappings:
        if getattr(item, attrname) == given:
            return item
    return None

def is_gtype_valid(the_dtype):
    if not isinstance(the_dtype, np.dtype):
        return False
    return the_dtype in _modgpu_supported_dtypes

