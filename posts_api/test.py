import math
def karatsuba(x, y):
    n = len(str(x))

    if n == 1:
        return x*y
    else:
        m = math.ceil(n/2)
        x1 = math.floor(x/(pow(10, m)))
        y1 = math.floor(y/(pow(10, m)))
        x2 = x%(pow(10, m))
        y2 = y%(pow(10, m))
        tmp1 = karatsuba(x1, y1)
        tmp2 = karatsuba(x2, y2)
        tmp3 = karatsuba(x1+x2, y1+y2) - tmp1 - tmp2

    return tmp1*(pow(10, n)) + tmp3*(pow(10, m)) +tmp2

print(karatsuba(755, 211))

