def isinteger(s):
    return s.isdigit() or \
           s != '' and s[0] == '-' and s[1:].isdigit() or\
           s != '' and s[0] == '+' and s[1:].isdigit()

def isfixed(s):
    (num, dot, fraction) = s.partition('.')
    return dot == '' and isinteger(num) and fraction == '' or\
           ((num == '' or num == '-') and fraction.isdigit() or\
           isinteger(num) and (fraction == '' or fraction.isdigit()))

def isfloat(s):
    (significand, e, exponent) = s.partition('e')
    return e == '' and exponent == '' and isfixed(significand) or\
           e == 'e' and isfixed(significand) and isinteger(exponent)
           
print(isfloat("2"))
print(isfloat("-2"))
print(isfloat(".112"))
print(isfloat("-.112"))
print(isfloat("3.14"))
print(isfloat("-3.14"))
print(isfloat("5."))
print(isfloat("5.0"))
print(isfloat("-777.0"))
print(isfloat("-777."))
print(isfloat("."))
print(isfloat(".."))
print(isfloat("0e3"))
print(isfloat("1.3e0"))
print(isfloat("1.3e0"))
print(isfloat("1e3"))
print(isfloat("1.314e4"))
print(isfloat("-1.1e-2"))
print(isfloat(".3e4"))
print(isfloat("2.e-2"))
print(isfloat("0e3"))
