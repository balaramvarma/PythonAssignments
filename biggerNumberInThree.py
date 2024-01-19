a=int(input("enter a 1st number\n"))
b=int(input("enter a 2nd number\n"))
c=int(input("enter a 3rd number\n"))

if a>b and a>c:
    print("{} is bigger number than {} and {}".format(a,b,c))
elif b>a and b>c:
    print("{} is bigger number than {} and {}".format(b,a,c))
else:
    print("{} is bigger number than {} and {}".format(c,a,b))