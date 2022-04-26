def solitary(xs):
    if len(xs) < 2:
        return True
    elif xs[0] in xs[1:]:
        return False
    else:
        return solitary(xs[1:])

print(solitary('12334'))

def solitary(xs):
    return len(xs) < 2 or xs[0] not in xs[1:] and solitary(xs[1:])

print(solitary('1234555'))
    