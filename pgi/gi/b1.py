def distanced(xs):
    if len(xs) < 2:
        return True
    elif xs[0] == xs[1]:
        return False
    else:
        return distanced(xs[1:])

def distance(xs):
    if len(xs) > 1:
        if xs[0] == xs[1]:
            return False
        else:
            return distance(xs[1:])
    return True


def distanced(xs):
    return len(xs) == 1 or xs[0] != xs[1] and distanced(xs[1:])

