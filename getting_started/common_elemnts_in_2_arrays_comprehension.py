arr1=[1,2,4,5,6,7,8,9,3]
arr2=[2,4,6,8,10,12,14,16,18,20]

def arr_common(arr1,arr2):
    arr3=[item for item in arr1 if item in arr2 ]
    return arr3

print(arr_common(arr1,arr2))
