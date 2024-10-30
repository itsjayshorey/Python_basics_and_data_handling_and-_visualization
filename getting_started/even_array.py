def array(arr):
    ar=[]
    for el in arr:
        if(el%2==0):
            ar.append(el)
    return ar

arr=[]
a=int(input())
for el in range(a):
    q=int(input())
    arr.append(q)
print(array(arr))