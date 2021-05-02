def _arraySum(array):
    sum=0
    for i in array:
        sum=sum+i
    return sum
array=[]
array=[12,13,14,45]
res=_arraySum(array)
print(f"Addition of array element is:{res}")

