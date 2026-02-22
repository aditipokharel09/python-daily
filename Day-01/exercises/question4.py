import numpy as np
point_a = np.array([2,3])
point_b = np.array([10,8])

diff =  point_b - point_a
squared_diff = diff ** 2
sum_squares = np.sum(squared_diff)
distance = np.sqrt(sum_squares)
print(f"the euclidean distance is:{distance}")
