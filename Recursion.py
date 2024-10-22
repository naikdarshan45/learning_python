def function(x):
    if x==0:
        return 1
    else:
        return function(x)- 1

x=9 
for i in range(10):
    print(function(i))