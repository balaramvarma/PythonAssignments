l=[1,5,7,3,8,5,9]
y=l.sort()
print(y)
print(l)

o=[2,6,3,7,543,3]
o.sort(reverse=True)
print(o)

def myFunc(a):
    return len(a)
h=["ghgy","hh","gihu","rama"]
h.sort(key=myFunc)
print(h)