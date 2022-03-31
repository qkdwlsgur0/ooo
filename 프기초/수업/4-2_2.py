def isinteger(s):
    return s.isdigit() or \
           s != '' and s[0] == '-' and s[1:].isdigit()

def isfloat(s):
    (left, dot, right) = s.partition('.')
    return dot == '' and isinteger(left) and right == '' or\
           dot == '.' and\
           ((left == '' or left == '-') and right.isdigit() or\
           isinteger(left) and (right == '' or right.isdigit()))

print(isfloat('.112'))
print(isfloat('-.112'))
print(isfloat('3.14'))
print(isfloat('-3.14'))
print(isfloat('5.'))
print(isfloat('5.0'))
print(isfloat('-777.0'))
print(isfloat('-777.'))
print(isfloat('.'))
print(isfloat('..'))