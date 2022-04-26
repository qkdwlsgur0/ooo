def remove_deplicates(xs):
    if xs != []:
        if xs[0] in xs[1:]:
            return remove_deplicates(xs[1:])
        else:
            return [xs[0]]+remove_deplicates(xs[1:])
    else:
        return []

def remove_duplicates(xs):
    def loop(xs,left):
        if xs != []:
            if xs[0] in xs[1:]:
                return loop(xs[1:],left)
            else:
                return loop(xs[1:],left+[xs[0]])
        else:
            return left
    return loop(xs,[])

def remove_duplicates(xs):
    left = []
    while xs != []:
        if xs[0] in xs[1:]:
            xs = xs[1:]
        else:
            left += [xs[0]]
            xs = xs[1:]
    return left

print(remove_deplicates([1,1,1,1,1,1,2,2,3,2]))