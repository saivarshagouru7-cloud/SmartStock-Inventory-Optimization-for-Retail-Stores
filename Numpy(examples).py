import numpy as np
# 1-D array
A = np.array([1,2,3,4,5])
print("one dimension array:\n",A)
# 2-D array
B = np.array([[1,2],[3,4]])
print("two-D array:\n",B)
#create array with full of zeros
S = np.full((3,4),0)
print("Arry of zeros:\n",S)
#mathmetical operations
M = np.array([1,2,3,4,5])
N = np.array([1,2,3,4,5])
print("Addtion:\n",M+N)
print("Subsraction:\n",M-N)
print("Multiplication:\n",M*N)
print("Division:\n",M/N)
print("Square of array:\n",M**2)
print("Square root of array:\n",np.sqrt(M))
print("Exponetial of array:\n",np.exp(M))
print("Sign change of array:\n",-M)
#Satistical operations of array
M = np.array([1,2,3,4,5])
print("Mean of array:\n",M.mean())
print("Total of array:\n",M.sum())
print("Median of array:\n",np.median(M))
print("Standared deviation of array:\n",M.std())
print("variance of array:\n",M.var())


