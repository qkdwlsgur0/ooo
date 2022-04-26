def union(l1,l2):
    if l1 != []:
        if l1[0] in l2:
            return union(l1[1:],l2)
        else:
            return [l1[0]]+union(l1[1:],l2)
    else:
        return l2

def union(l1,l2):
    def loop(l1,left):
        if l1 != []:
            if l1[0] in l2:
                return loop(l1[1:],left)
            else:
                return loop(l1[1:],left+[l1[0]])
        else:
            return left+l2
    return loop(l1,[])

def union(l1,l2):
    left = []
    while l1 != []:
        if l1[0] in l2:
            l1 = l1[1:]
        else:
            left += [l1[0]]
            l1 = l1[1:]
    return left+l2


def union(l1,l2):
    left = []
    for i in l1:
        if i not in l2:
            left += [i]
    return left+l2



print(union([1,2,3,4,5],[6,1,2,3]))