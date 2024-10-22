arr=[9,5,3,2,1]
n=len(arr)
for i in range(n-1,-1,-1):
    bo=0
    for j in range(0,i):
        if arr[j]>arr[j+1]:
            bo=1
            arr[j],arr[j+1]=arr[j+1],arr[j]
 

print(arr)
    


