#1)
import numpy as np
x=np.random.rand(10,1)
#print(x)
print("mean is:",np.mean(x))

#2)
import numpy as np
y=np.random.rand(20,1)
print(y)
print("Standard deviation is:",np.std(y))
print("Variance is:",np.var(y))

#3)
import numpy as np
A=np.random.rand(10,20)
B=np.random.rand(20,25)
C=np.matmul(A,B)
print("Multiplication of matrix A*B is:",C)
print("Shape of new matrix:",C.shape)
print("Sum of all the element of new matrix:",np.sum(C))


#4)
import math
import numpy as np
ar_A=np.random.rand(10,1)
print("array:\n",ar_A,"\n")
def my_func(x):
    return(1/(1+math.exp(-x)))
ar_B=np.array((list(map(my_func,ar_A))))
print("result is:",ar_B)

