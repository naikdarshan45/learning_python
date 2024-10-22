arr=[10,8,2,3,1,4]
l=len(arr)-1
n=len(arr)

for i in range(0,l):
    index=i
    for j in range(i+1,n):
        if arr[j]<arr[index]:
            index=j
    arr[i],arr[index]=arr[index],arr[i]
print(arr)

        