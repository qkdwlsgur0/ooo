def head_equiv(xs):
    if len(xs) > 1:
        if xs[0] == xs[1]:
            return [xs[0]]+head_equiv(xs[1:])
        else:
            return [xs[0]]
    else:
        return xs


def head_equiv(xs):
    def loop(xs,head):
        if len(xs) > 1:
            if xs[0] == xs[1]:
                return loop(xs[1:],head+[xs[0]])
            else:
                return head+[xs[0]]
        else:
            return head+xs
    return loop(xs,[])
        
def head_equiv(xs):
    head = []
    while len(xs) > 1:
        if xs[0] == xs[1]:
            head += [xs[0]]
            xs = xs[1:]
        else:
            return head+[xs[0]]
    return head+xs
