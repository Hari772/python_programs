#  Inverse of a given Matrix
import numpy as np
a=np.array([[1,2],[3,4]])
print("Original matrix: ")
print(a)
result=np.linalg.inv(a)
print("inverse  matrix is:")
print(result)