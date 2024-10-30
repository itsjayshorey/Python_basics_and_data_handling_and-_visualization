import numpy as np 
a=int(input())
arr=[]
for i in range(a):
    k=int(input())
    arr.append(k)
for el in arr:
    t=True
    for ele in range(2,int(np.sqrt(el))):
        if el % ele ==0:
            t=False
            break
    if t:
        print(el)
    