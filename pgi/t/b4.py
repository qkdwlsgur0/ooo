def difference(xs,ys):
    if xs != []:
        if xs[0] in ys:
            return difference(xs[1:],ys)
        else:
            return [xs[0]]+difference(xs[1:],ys)
    else:
        return []

def difference(xs,ys):
    def loop(xs,left):
        if xs != []:
            if xs[0] in ys:
                return loop(xs[1:],left)
            else:
                return loop(xs[1:],left+[xs[0]])
        else:
            return left
    return loop(xs,[])

def difference(xs,ys):
    left = []
    while xs != []:
        if xs[0] in ys:
            xs = xs[1:]
        else:
            left += [xs[0]]
            xs = xs[1:]
    return left

def difference(xs,ys):
    left = []
    for i in xs:
        if i not in ys:
            left += [i]
    return left

print(difference([],[1,3,4,5,7,8,9]))