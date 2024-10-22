#maximum and minmum in an array
# arr=[4,5,2,8]
# max=0

# n=len(arr)
# for i in range(n):
#     if max<arr[i]:
#         max=arr[i]

# print(f"maximum value in an array is :",max)


# index=0
# min=0

# n=len(arr)
# for i in range(n):
#     if arr[index]>=arr[i]:
#         min=arr[i]

# print(f"minmum value in an array is :",min)


#maximum and minmum in an array
# arr=[4,5,2,8]
# max=0
# index=0
# min=0

# n=len(arr)
# for i in range(n):
#     if max<arr[i]:
#         max=arr[i]
#     if arr[index]>=arr[i]:
#         min=arr[i]

# print(f"maximum value in an array is :",max)
# print(f"minmum value in an array is :",min)



##linear search
# arr=[10,20,43,23,45,65,67]
# target =65
# for i in range(len(arr)):
#     if target==arr[i]:
#         print(f"index",i,"target",target)

##reverse an even array
# arr=[2,7,5,9,8]
# n=len(arr)-1
# i=0
# j=n
# while i<=j:
#     arr[i],arr[j]=arr[j],arr[i]
#     i+=1
#     j-=1
    
# print(arr)

## reverse an odd array



## reversal of list
#Approach: Two pointer
#input:[1,4,6,8,11]
#output:[11,8,6,4,1]

#function defination
# def reverse(arr):
#     #write your own code

#     # return arr[::-1]
    
#     # ans=[]
#     # for i in range(1,len(arr)+1):
#     #     ans.append(arr[-i])
#     # return ans

#     n=len(arr)-1
#     i=0
#     j=n
#     while i < j:
#         arr[i], arr[j] = arr[j], arr[i]
#         i=i+1
#         j=j-1
#     return arr

# Driver Code
# arr=[1,4,6,8,11]
# result=reverse(arr)
# print(result)

## write a fuction to segregate even odd number
#Approach: partiton Array
#input:[7,2,9,4,6,1,3,8,5]
#output:[2,4,6,8,7,9,1,3,5]
# def segregate(arr):
#     i = -1
#     j = 0
#     n=len(arr)
#     while j!=n:
#         if(arr[j]%2==0):
#             i=i+1
#             arr[i], arr[j] = arr[j], arr[i]
#         j=j+1
#     return arr


# arr=[7,2,9,4,6,1,3,8,5]
# result=segregate(arr)
# print(result)


# even=[5,2,9,4,7,6,1,0]
# odd=[11,33,9,76,43]
# n=len(even)-1
# print(even)
# i=0
# while i<n:
#     if i+1<n:
#         even[i],even[i+1]=even[i+1],even[i]
        
#     i+=2
# print(even)


# arr=[4,3,7,2]
# n=len(arr)
# sub=[]
# for i in range(n):
#     for j in range(i + 1, n + 1):
#         sub.append(arr[i:j])
# print(sub)

# arr=[3,4,-2,5,8,20,-10,8]
# total_sum=0
# n=len(arr)
# prefix=0
# for i in range(n):
#     total_sum+=arr[i]
# for i in range(n-1):
#     prefix+=arr[i]
#     ans=total_sum-prefix
#     if ans==prefix:
#         print(1)

# arr=[4,3,7,2]
# n=len(arr)
# for i in range(n+1):
#     for j in range(i,n+1):
#         for k in range(i,j):
#             print(arr[k])
#         print(" ")
    
# arr=[4,2,5,2,6]
# n=len(arr)
# for i in range(n+1):
#     for j in range(i,n+1):
#         for k in range(j):
#             print(arr[k], end=" ")
#     print()

arr=[4,2,5,2,6]
n=len(arr)
mx1=0
for i in range(n+1):
    cu=0
    for j in range(i,n):
        cu+=arr[j]
        mx1=max(cu,mx1)

print(mx1)


