def union(xs,ys):
    if xs != []:
        if xs[0] in ys:
            return union(xs[1:],ys)
        else:
            return [xs[0]]+union(xs[1:],ys)
    else:
        return ys

def union_2(xs,ys):
    def loop(xs,left):
        if xs != []:
            if xs[0] in ys:
                return loop(xs[1:],left)
            else:
                return loop(xs[1:],left+[xs[0]])
        else:
            return left+ys
    return loop(xs,[])

def union_3(xs,ys):
    left = []
    while xs != []:
        if xs[0] in ys:
            xs = xs[1:]
        else:
            left += [xs[0]]
            xs = xs[1:]
    return left+ys

def union_4(xs,ys):
    left = []
    for i in xs:
        if i in ys:
            xs = xs[1:]
        else:
            left += [i]
            xs = xs[1:]
    return left+ys

# Test code    
print(union([],[]))           # []
print(union([1,2],[]))        # [1, 2]
print(union([],[3,4]))        # [3, 4]
print(union([1,2],[3,4]))     # [1, 2, 3, 4]
print(union([1,2],[2,3]))     # [1, 2, 3]
print(union([1,2],[2,1]))     # [2, 1]
print(union([1,2,3],[3,2,1])) # [3, 2, 1]
print(union([1,2,3],[3,2,4])) # [1, 3, 2, 4]
print(union([1,2,3],[4,5,6])) # [1, 2, 3, 4, 5, 6]