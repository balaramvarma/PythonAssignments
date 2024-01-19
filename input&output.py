#input statements
a=input("enter a string")
print(a)

b=int(input("enter a number"))
print(b)

c=input("enter a sequence").split()
print(c)

#output statements

name="rama"
cname="solutions"

print(f"{name} is software engineer in {cname}")
print("{} is software engineer in {}".format(name,cname))
print("{0} is software engineer in {1}".format(name,cname))
print("{a} is software engineer in {b}".format(a=name,b=cname))