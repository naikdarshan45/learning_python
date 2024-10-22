
###finding index in 2d array
# index=row_index*column+column_index

### how to find the row_index and column_index from given array value(666)
##if index is given in condition
# row_index:index/column
# column_index:index%column


li=[[123,343,555],
    [435,565,243]]
l=len(li)
r=len(li[0])
for i in range(l):
    for j in range(r):
        print(li[i][j])
print(li)