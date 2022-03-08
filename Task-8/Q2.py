import numpy as np
A = np.array([1 ,0, 0, 0 ,1, 0])
B = np.array([0 ,0, 1, 1 ,0 ,1])
array_len=len(A)
for i in range(array_len):
    if A[i] == B[i] :       #checking each elemnt in arrays consecutively
        result=0
    else :
        result=1
if result==0:
    
    print("Arrays are equal ")
else :
    
    print("Arrays are not equal ")