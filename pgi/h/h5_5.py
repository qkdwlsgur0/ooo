def intersection(xs,ys):
    if xs != []:
        if xs[0] in ys:
            return [xs[0]]+intersection(xs[1:],ys)
        else:
            return intersection(xs[1:],ys)
    else:
        return []

def intersection_2(xs,ys):
    def loop(xs,left):
        if xs != []:
            if xs[0] in ys:
                return loop(xs[1:],left+[xs[0]])
            else:
                return loop(xs[1:],left)
        else:
            return left
    return loop(xs,[])

def intersection_3(xs,ys):
    left = []
    while xs != []:
        if xs[0] in ys:
            left += [xs[0]]
            xs = xs[1:]
        else:
            xs = xs[1:]
    return left

def intersection_4(xs,ys):
    left = []
    for i in xs:
        if i in ys:
            left += [i]
            xs = xs[1:]
        else:
            xs = xs[1:]
    return left


# Test code    
print(intersection([],[]))           # []
print(intersection([1,2],[]))        # []
print(intersection([],[3,4]))        # []
print(intersection([1,2],[3,4]))     # []
print(intersection([1,2],[2,3]))     # [2]
print(intersection([1,2],[2,1]))     # [1, 2]
print(intersection([1,2,3],[3,2,1])) # [1, 2, 3]
print(intersection([1,2,3],[3,2,4])) # [2, 3]
print(intersection([1,2,3],[4,5,6])) # []