n=int(input("Enter a Number :\n"))
countd=0
while n!=0:
    n=n//10
    countd+=1
print("Count the total number of digits in a number :",countd)