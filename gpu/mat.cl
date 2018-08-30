__kernel void sum(__global const float *a_g, __global const float *b_g, __global float *res_g)
{
  int gid = get_global_id(0);
  res_g[gid] = a_g[gid] + b_g[gid];
}
__kernel void sum_scaler(__global const float *a_g, __global const float b, __global float *res_g)
{
  int gid = get_global_id(0);
  res_g[gid] = a_g[gid] + b;
}
__kernel void sum_by_scaler(__global const float a, __global const float *b_g, __global float *res_g)
{
    int gid = get_group_id(0);
    res_g[gid] = a + b[gid];
}


__kernel void sub(__global const float *a_g, __global const float *b_g, __global float *res_g)
{
  int gid = get_global_id(0);
  res_g[gid] = a_g[gid] - b_g[gid];
}
__kernel void sub_scaler(__global const float *a_g, __global const float b, __global float *res_g)
{
  int gid = get_global_id(0);
  res_g[gid] = a_g[gid] - b;
}
__kernel void sub_by_scaler(__global const float a, __global const float *b_g, __global float *res_g)
{
    int gid = get_group_id(0);
    res_g[gid] = a - b[gid];
}


__kernel void mul(__global const float *a_g, __global const float *b_g, __global float *res_g)
{
  int gid = get_global_id(0);
  res_g[gid] = a_g[gid] * b_g[gid];
}
__kernel void mul_scaler(__global const float *a_g, __global const float b, __global float *res_g)
{
  int gid = get_global_id(0);
  res_g[gid] = a_g[gid] * b;
}
__kernel void mul_by_scaler(__global const float a, __global const float *b_g, __global float *res_g)
{
    int gid = get_group_id(0);
    res_g[gid] = a * b[gid];
}


__kernel void div(__global const float *a_g, __global const float *b_g, __global float *res_g)
{
  int gid = get_global_id(0);
  res_g[gid] = a_g[gid] / b_g[gid];
}
__kernel void div_scaler(__global const float *a_g, __global const float b, __global float *res_g)
{
  int gid = get_global_id(0);
  res_g[gid] = a_g[gid] / b;
}
__kernel void div_by_scaler(__global const float a, __global const float *b_g, __global float *res_g)
{
    int gid = get_group_id(0);
    res_g[gid] = a / b[gid];
}
