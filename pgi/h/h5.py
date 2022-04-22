#__________ 5-1 _______________________________________

def remove_one(x,xs):
    if xs != []:
        if x == xs[0]:
            return xs[1:]
        else:
            return [xs[0]]+remove_one(x,xs[1:])
    else:
        return []

def remove_one(x,xs):
    def loop(xs,ss):
        if xs != []:
            if x == xs[0]:
                return ss+xs[1:]
            else:
                return loop(xs[1:],ss+[xs[0]])
        else:
            return ss
    return loop(xs,[])

def remove_one(x,xs):
    ss = []
    while xs != []:
        if x == xs[0]:
            return ss+xs[1:]
        else:
            ss.append(xs[0]) # += [xs[0]]
            xs = xs[1:]
    return ss


#__________ 5-2 _______________________________________

def remove_all(x,xs):
    if xs != []:
        if x == xs[0]:
            return remove_all(x,xs[1:])
        else:
            return [xs[0]]+remove_all(x,xs[1:])
    else:
        return []

def remove_all(x,xs):
    def loop(xs,ss):
        if xs != []:
            if x != xs[0]:
                ss.append(xs[0])
            return loop(xs[1:],ss)
        else:
            return ss
    return loop(xs,[])

def remove_all(x,xs):
    ss = []
    while xs != []:
        if x == xs[0]:
            xs = xs[1:]
        else:
            ss.append(xs[0])
            xs = xs[1:]
    return ss


#__________ 5-3 _______________________________________

def remove_duplicates(xs):
    if len(xs) >= 2:
        head = xs[0]
        return [head]+remove_duplicates(remove_all(head,xs))
    else:
        return xs

def remove_duplicates(xs):
    def loop(xs,ss):
        if len(xs) >= 2:
            head = xs[0]
            return loop(remove_all(head,xs),ss+[head])
        else:
            return ss+xs
    return loop(xs,[])
    
def remove_duplicates(xs):
    ss = [] 
    while len(xs) >= 2:
        head = xs[0]
        ss.append(head)
        xs = remove_all(head,xs)
    return ss+xs


#__________ 5-4 _______________________________________

def union(xs,ys):
    if xs != []:
        if xs[0] in ys:
            return union(xs[1:],ys)
        else:
            return [xs[0]]+union(xs[1:],ys)
    else:
        return ys

def union(xs,ys):
    def loop(xs,ss):
        if xs != []:
            if xs[0] not in ys:
                ss.append(xs[0])
            return loop(xs[1:],ss)
        else:
            return ss+ys
    return loop(xs,[])

def union(xs,ys):
    ss = []
    while xs != []:
        if xs[0] in ys:
            xs = xs[1:]
        else:
            ss.append(xs[0])
            xs = xs[1:]
    return ss+ys

def union(xs,ys):
    ss = []
    for i in xs:
        if i in ys:
            xs = xs[1:]
        else:
            ss.append(i)
            xs = xs[1:]
    return ss+ys


#__________ 5-5 _______________________________________

def intersection(xs,ys):
    if xs != []:
        if xs[0] in ys:
            return [xs[0]]+intersection(xs[1:],ys)
        else:
            return intersection(xs[1:],ys)
    else:
        return []

def intersection(xs,ys):
    def loop(xs,ss):
        if xs != []:
            if xs[0] in ys:
                ss.append(xs[0])
            return loop(xs[1:],ss)
        else:
            return ss
    return loop(xs,[])

def intersection(xs,ys):
    ss = []
    while xs != []:
        if xs[0] in ys:
            ss.append(xs[0])
            xs = xs[1:]
        else:
            xs = xs[1:]
    return ss

def intersection(xs,ys):
    ss = []
    for i in xs:
        if i in ys:
            ss.append(i)
            xs = xs[1:]
        else:
            xs = xs[1:]
    return ss

#__________ 5-6 _______________________________________

def difference(xs,ys):
    if xs != []:
        if xs[0] in ys:
            return difference(xs[1:],ys)
        else:
            return [xs[0]]+difference(xs[1:],ys)
    else:
        return []

def difference(xs,ys):
    def loop(xs,ss):
        if xs != []:
            if xs[0] not in ys:
                ss.append(xs[0])
            return loop(xs[1:],ss)
        else:
            return ss
    return loop(xs,[])

def difference(xs,ys):
    ss = []
    while xs != []:
        if xs[0] in ys:
            xs = xs[1:]
        else:
            ss.append(xs[0])
            xs = xs[1:]
    return ss

def difference(xs,ys):
    ss = []
    for i in xs:
        if i not in ys:
            ss.append(i)
    return ss


