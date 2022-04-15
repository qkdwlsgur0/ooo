def selection_sort_1(xs):
    if xs != []:
        smallest = min(xs)
        xs.remove(smallest)
        return [smallest] + selection_sort_1(xs)
    else:
        return []

def selection_sort_2(xs):
    def loop(xs,ss):
        if xs != []:
            smallest = min(xs)
            xs.remove(smallest)
            ss.append(smallest)
            return loop(xs,ss)
        else:
            return ss
    return loop(xs,[])

def selection_sort_3(xs):
    ss = []
    while xs != []:
        smallest = min(xs)
        xs.remove(smallest)
        ss.append(smallest)
    return ss

print(selection_sort_3([9,8,7,6,5,4,3,2,1]))


def insert_1(x,ss):
    if ss != []:
        if x <= ss[0]:
            return [x]+ss
        else:
            return [ss[0]] + insert_1(x,ss[1:])
    else:
        return [x]

print(insert_1(9,[2,4,5,7]))

def insert_2(x,ss):
    def loop(ss,left):
        if ss != []:
            if x <= ss[0]:
                return left+[x]+ss
            else:
                return loop(ss[1:],left+[ss[0]])
        else:
            return left + [x]
    return loop(ss,[])


def insert_3(x,ss):
    left = []
    while ss != []:
        if x <= ss[0]:
            return left+[x]+ss
        else:
            left.append(ss[0])
            ss = ss[1:]
    left.append(x)
    return left

            
print(insert_3(9,[2,4,5,7]))