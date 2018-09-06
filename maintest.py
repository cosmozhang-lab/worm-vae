from gpu import Mat
import numpy as np

# ga1 = Mat(np.arange(12).reshape([4,3]))
# ga2 = Mat(ga1)

# ga1 = Mat(np.arange(12).reshape([4,3]))
# ga2 = Mat(np.arange(15).reshape([3,5]))

# print((ga1 @ ga2).gather())

ga1 = Mat(np.arange(12))
ga2 = ga1.reshape([3,4])
ga3 = ga1.reshape([3,4])
ga3 += ga2
ga4 = ga2.T
print("ga1:")
print(ga1.gather())
print("ga2:")
print(ga2.gather())
print("ga3:")
print(ga3.gather())
print("ga4:")
print(ga4.gather())
