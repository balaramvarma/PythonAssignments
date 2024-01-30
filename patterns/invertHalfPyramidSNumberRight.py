n=int(input("Enter a Number:\n"))

for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(n-i):
        print(k+1,end=" ")
    print()