def difference(xs,ys):
    if xs != []:
        if xs[0] in ys:
            return difference(xs[1:],ys)
        else:
            return [xs[0]]+difference(xs[1:],ys)
    else:
        return []

def difference_2(xs,ys):
    def loop(xs,left):
        if xs != []:
            if xs[0] in ys:
                return loop(xs[1:],left)
            else:
                return loop(xs[1:],left+[xs[0]])
        else:
            return left
    return loop(xs,[])

def difference_3(xs,ys):
    left = []
    while xs != []:
        if xs[0] in ys:
            xs = xs[1:]
        else:
            left += [xs[0]]
            xs = xs[1:]
    return left

def difference_4(xs,ys):
    left = []
    for i in xs:
        if i in ys:
            xs = xs[1:]
        else:
            left += [i]
            xs = xs[1:]
    return left


# Test code    
print(difference([],[]))           # []
print(difference([1,2],[]))        # [1, 2]
print(difference([],[3,4]))        # []
print(difference([1,2],[3,4]))     # [1, 2]
print(difference([1,2],[2,3]))     # [1]
print(difference([1,2],[2,1]))     # []
print(difference([1,2,3],[3,2,1])) # []
print(difference([1,2,3],[3,2,4])) # [1]
print(difference([1,2,3],[4,5,6])) # [1, 2, 3]