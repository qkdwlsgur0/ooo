def smaller(x,y):
    if (x<y):
        return x
    else:
        return y

def smallest(x,y,z,a):
    return smaller(smaller(smaller(x,y),z),a)

print(smallest(390,399,389,388))