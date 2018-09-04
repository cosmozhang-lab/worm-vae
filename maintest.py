from gpu import Mat
import numpy as np

ga1 = Mat(np.arange(12).reshape([4,3]))
ga2 = Mat(ga1)

# ga1 = Mat(np.arange(12).reshape([4,3]))
# ga2 = Mat(np.arange(15).reshape([3,5]))

# print((ga1 @ ga2).gather())
