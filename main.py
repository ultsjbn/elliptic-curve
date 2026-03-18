# Use instead of division because division isnt allowed in modular arithmetic
def modular_inverse(n, p):
    return pow(n, p-2, p)

def operations(a, p, P, Q):
    #case where some points are infinity
    if P is None:
        return Q
    if Q is None:
        return P
    
    x1, y1 = P
    x2, y2 = Q

    # Reference is libro sa gclass, pg. 244 

    # Addition if P not equal to Q
    # Point addition
    # s = (y2-y1)/(x2-x1)

    # Doubling if P equal to Q
    # Point doubling
    # s = (3(x1)^2+a)/2y1

    #  case where P + (-P) = PaI
    if x1 == x2 and (y1 + y2) % p == 0:
            return None  # PaI

    if x1 == x2 and y1 == y2:
        if y1 == 0:
             return None #PaI since y1 = 0 is tangent
        numerator = (3 * pow(x1, 2) + a)
        denominator = modular_inverse(2 * y1, p)
    else:
        numerator = (y2 - y1)
        denominator = modular_inverse(x2-x1, p)

    s = (numerator * denominator) % p

    x3 = (pow(s, 2) - x1 - x2) % p
    y3 = (s * (x1-x3) - y1) % p

    return (x3, y3)

#bale None irereturn niya pag infinity siya, gawa nalang function to print P + Q = Point at Infinity or some shit like that

# error handling for if hindi integer input
def get_number(prompt):
    while True:
         try:
             return int(input(prompt))
         except ValueError:
             print("Input is not an integer.")

if __name__ == "__main__":
    # get user input
    print("Enter parameters:\n")
    p = get_number("Enter p: ")
    a = get_number("Enter a: ")
    b = get_number("Enter b: ")
    
    print("\nEnter Point P (x1, y1):\n")
    x1 = get_number("x1: ")
    y1 = get_number("y1: ")
    
    print("\nEnter Point Q (x2, y2):\n")
    x2 = get_number("x2: ")
    y2 = get_number("y2: ")
    
    point_p = (x1, y1)
    point_q = (x2, y2)

    result = operations(a, p, point_p, point_q)

    print("\nResult: ",result)