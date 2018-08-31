import pyopencl as cl
import numpy as np
from essentials import program, ctx
from dtypes import _modgpu_supported_dtype_gputype_mappings

class BaseOperatorForType:
    def __init__(self, clprg):
        self.kernel_base = clprg.op
        self.kernel_scalar = clprg.op_scalar
        self.kernel_byscalar = clprg.op_byscalar

class BaseOperator:
    def __init__(self, clprgs):
        for k in clprgs:
            setattr(self, k, clprgs[k])

def _build_base_operator(name, clexpr):
    clfuncs = dict()
    for dtypeitem in _modgpu_supported_dtype_gputype_mappings:
        gtype = dtypeitem[0]
        gputype = dtypeitem[1]
        prg = cl.Program(ctx, """
            __kernel void op(__global const """ + gputype + """ *a_g, __global const """ + gputype + """ *b_g, __global """ + gputype + """ *res_g)
            {
                int gid = get_global_id(0);
                res_g[gid] = """ + clexpr.replace("a", "a_g[gid]").replace("b", "b_g[gid]") + """;
            }
            __kernel void op_scalar(__global const """ + gputype + """ *a_g, __global const """ + gputype + """ b, __global """ + gputype + """ *res_g)
            {
                int gid = get_global_id(0);
                res_g[gid] = """ + clexpr.replace("a", "a_g[gid]").replace("b", "b") + """;
            }
            __kernel void op_byscalar(__global const """ + gputype + """ a, __global const """ + gputype + """ *b_g, __global """ + gputype + """ *res_g)
            {
                int gid = get_group_id(0);
                res_g[gid] = """ + clexpr.replace("a", "a").replace("b", "b_g[gid]") + """;
            }""").build()
        clfuncs[gtype] = BaseOperatorForType(prg)
    return clfuncs

base_operator_add = _build_base_operator("add", "a + b")
base_operator_sub = _build_base_operator("sub", "a - b")
base_operator_mul = _build_base_operator("mul", "a * b")
base_operator_div = _build_base_operator("div", "a / b")
base_operator_eq = _build_base_operator("eq", "a == b")
base_operator_lt = _build_base_operator("lt", "a < b")
base_operator_le = _build_base_operator("le", "a <= b")
base_operator_gt = _build_base_operator("gt", "a > b")
base_operator_ge = _build_base_operator("ge", "a >= b")
base_operator_and = _build_base_operator("and", "a & b")
base_operator_or = _build_base_operator("or", "a | b")
base_operator_xor = _build_base_operator("xor", "a ^ b")




