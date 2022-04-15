def remove_one(x,xs):
    if xs != []:
        if x == xs[0]:
            return xs[1:]
        else:
            return [xs[0]]+remove_one(x,xs[1:])
    else:
        return []

def remove_one_2(x,xs):
    def loop(xs,left):
        if xs != []:
            if x == xs[0]:
                return left+xs[1:]
            else:
                return loop(xs[1:],left+[xs[0]])
        else:
            return left
    return loop(xs,[])

def remove_one_3(x,xs):
    left = []
    while xs != []:
        if x == xs[0]:
            return left+xs[1:]
        else:
            left += [xs[0]]
            xs = xs[1:]
    return left

# Test code
print(remove_one(3,[]))        # []
print(remove_one(3,[3]))       # []
print(remove_one(3,[2]))       # [2]
print(remove_one(3,[2,3,2,3])) # [2, 2, 3]
print(remove_one(3,[2,2,2,3])) # [2, 2, 2]
print(remove_one(3,[2,2,2,2])) # [2, 2, 2, 2]