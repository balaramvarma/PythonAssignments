n=int(input("Enter a Number:\n"))

for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()