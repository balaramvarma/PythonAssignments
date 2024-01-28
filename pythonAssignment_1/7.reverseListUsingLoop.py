n=list(map(int,input("Enter a List:\n").split()))
m=[]
for i in n:
    m=[i]+m
print("reverse order of list :",m)