# Use instead of division because division isnt allowed in modular arithmetic
def modular_inverse(n, p):
    return pow(n, p-2, p)

def operations(a, p, P, Q):
    P = x1, y1
    Q = x2, y2

    # Reference is libro sa gclass, pg. 244 
    # wala pa case for neutral element (infinity) 

    # Addition if P not equal to Q
    # Point addition
    # s = (y2-y1)/(x2-x1)

    # Doubling if P equal to Q
    # Point doubling
    # s = (3(x1)^2+a)/2y1

    if x1 == x2 and y1 == y2:
        numerator = (3 * pow(x1, 2) + a)
        denonimator = modular_inverse(2 * y1, p)
    else:
        numerator = (y2 - y1)
        denominator = modular_inverse(x2-x1, p)

    s = (numerator * denominator) % p

    x3 = (pow(s, 2) - x1 - x2) % p
    y3 = (s * (x1-x3) - y1) % p

    return (x3, y3)

if __name__ == "__main__":
    # Manual input muna stinart q para madali test
    p = 19
    a = 6
    b = 7
    x1 = 2
    y1 = 3
    x2 = 4
    y2 = 2

    point_p = (x1, y1)
    point_q = (x2, y2)

    result = operations(a, p, point_p, point_q)

    print(result)