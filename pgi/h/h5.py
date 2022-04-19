#__________ 5-1 _______________________________________

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


#__________ 5-2 _______________________________________

def remove_all(x,xs):
    if xs != []:
        if x == xs[0]:
            return remove_all(x,xs[1:])
        else:
            return [xs[0]]+remove_all(x,xs[1:])
    else:
        return []

def remove_all_2(x,xs):
    def loop(xs,left):
        if xs != []:
            if x == xs[0]:
                return loop(xs[1:],left)
            else:
                return loop(xs[1:],left+[xs[0]])
        else:
            return left
    return loop(xs,[])

def remove_all_3(x,xs):
    left = []
    while xs != []:
        if x == xs[0]:
            xs = xs[1:]
        else:
            left += [xs[0]]
            xs = xs[1:]
    return left


#__________ 5-3 _______________________________________

def remove_all(x,xs):
    left = []
    while xs != []:
        if x == xs[0]:
            xs = xs[1:]
        else:
            left += [xs[0]]
            xs = xs[1:]
    return left


def remove_duplicates(xs):
    if len(xs) >= 2:
        head = xs[0]
        return [head]+remove_duplicates(remove_all(head,xs))
    else:
        return xs

def remove_duplicates_2(xs):
    def loop(xs,left):
        if len(xs) >= 2:
            head = xs[0]
            return loop(remove_all(head,xs),left+[head])
        else:
            return left+xs
    return loop(xs,[])
    
def remove_duplicates_3(xs):
    left = [] 
    while len(xs) >= 2:
        head = xs[0]
        left += [head]
        xs = remove_all(head,xs)
    return left+xs


#__________ 5-4 _______________________________________

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


#__________ 5-5 _______________________________________

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


#__________ 5-6 _______________________________________

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








