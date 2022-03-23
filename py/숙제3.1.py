def identical(x,y,z):
    if (x==y==z or x!=y!=z!=x):
        if (x==y==z):
            return (x, "triple")
        else:
            return None
    else:
        if (x==y):
            return (x, "twin")
        else:
            return (z, "twin")

print(identical(2,3,4))
print(identical(2,2,4))
print(identical(2,3,2))
print(identical(2,3,3))
print(identical(3,3,3))