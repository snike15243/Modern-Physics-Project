import numpy as np
import matplotlib.pyplot as plt

A=np.array([[1,1,1,1,1],
           [-2,-1,0,2,1],
           [4,1,0,1,4],
           [-8,-1,0,1,8],
           [16,1,0,1,16]])
b=np.array([0,1,0,0,0])

x=np.linalg.solve(A,b)

for i in range(21+1):
    print(i)
    print(x*i)

print(sum(x))
for i in range(5):
    print(np.transpose(A[i]))

    print(np.matmul(A[i],np.transpose(x)))

print(x)
print(f'1/12*{x*21}')