a,b=list(map(int,input("Enter a min and max numbers:\n").split()))
for i in range(a,b+1):
    c=0
    if i>1:
        for j in range(2,i):
            if i%j==0:
                c+=1
        if c==0:
            print(i)