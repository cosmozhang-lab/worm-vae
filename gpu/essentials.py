import pyopencl as cl

ctx = cl.create_some_context(interactive=False)
queue = cl.CommandQueue(ctx)

class Kernel:
    def __init__(self, clkernel):
        self.clkernel = clkernel

    def __call__(self, gsize, *args):
        clargs = [ctx, gsize, None] + args
        return apply(self.clkernel, clargs)

class Program:
    def __init__(self, clprogram):
        self.clprogram = clprogram
        kernel_names = clprogram.get_info(cl.program_info.KERNEL_NAMES).split(';')
        for kname in kernel_names:
            clkernel = getattr(clprogram, kname)
            setattr(self, kname, Kernel(clkernel))

def program(filename):
    fp = open(filename, 'r')
    filecontent = fp.read()
    fp.close()
    prg = cl.Program(ctx, filecontent).build()
    return Program(prg)
