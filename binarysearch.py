# arr=[3,4,5,6]
# target=6
# i=0
# n=len(arr)
# e=n-1
# while(i<=e):
#     mid=i+(e-e)//2
#     if arr[mid]==target:
        
#         print(mid)
#         break
#     elif arr[mid]<target:
#         i=mid+1
#     else:
#         e=mid-1


## TWO SUM PROBLEM
arr=[2,7,11,15,27]
target=22
n=len(arr)
s=0
ans=[]
for i in range(n):
    x=target-arr[i]
    start=0
    end=n-1
    
    while start<=end:
        mid=start+(end-start)//2
        if (arr[mid]<=x):
            s=mid
            start=mid+1
        else:
            end=mid-1
    if arr[s]+arr[i]==target:
        ans=[s,i]
        r=arr[s]+arr[i]
print(ans)
print(r)


        

    
            
