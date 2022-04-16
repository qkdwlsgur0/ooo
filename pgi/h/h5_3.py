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


# Test code    
print(remove_duplicates([]))                  # []
print(remove_duplicates([1]))                 # [1]
print(remove_duplicates([1,1]))               # [1]
print(remove_duplicates([1,1,1,1]))           # [1]
print(remove_duplicates([4,2,3,2,2,4,3,2,1])) # [4, 2, 3, 1]