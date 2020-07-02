from array import *

arr=array('i',[])

n=int(input("ENTER THE LENGTH OF ARRAY"))

for i in range(n):
    x=int(input("ENTER THE NEXT ELEMENT"))
    arr.append(x)

print(arr)
