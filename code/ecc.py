from utilities import modinv

# Consider a fixed elliptic curve E: y^2 = x^3 + ax + b over the field Z_p.
# Some of this code is only useful for small values of p.

p = 37
a = 2
b = 5

assert (4*a**3 + 27*b**2) % p != 0 # checking that the curve is regular

def on_curve(P):
    # Returns True if the point P = (x,y) lies on the elliptic curve
    if P == 'infinity':
        return True
    else:
        (x,y) = P
        return pow(y,2,p) == (pow(x,3,p) + a*x + b) % p

def reflect(P):
    # Returns P' (i.e. the negative of P)
    if P == 'infinity':
        return 'infinity'
    else:
        (x,y) = P
        return (x, (-y)%p)
    
def add(P,Q):
    # Returns the sum of P and Q
    if P == 'infinity':
        return Q
    if Q == 'infinity':
        return P
    (x1,y1) = P
    (x2,y2) = Q
    if Q == reflect(P):
        return 'infinity'
    if P != Q:
        rise = y2 - y1
        run = x2 - x1        
    if P == Q:
        rise = 3*x1**2 + a
        run = 2*y1
    slope = (rise * modinv(run,p)) % p
    x3 = (slope**2 - x1 - x2) % p
    y3 = (slope * (x1 - x3) - y1) % p
    return (x3,y3)

def mult(P,n):
    # Returns nP
    if P == 'infinity' or n == 0:
        return 'infinity'
    if n < 0:
        return mult(reflect(P), -n)
    # For n > 0, use the double-and-add algorithm:
    S = mult(add(P,P), n//2)
    if n % 2 == 0:
        return S
    else:
        return add(S,P)
    
def order(P):
    # Returns the order of a point P
    n = 1
    Power = P
    while Power != 'infinity':
        Power = add(Power, P)
        n += 1
    return n

def points_on_curve():
    # Returns the list of points on the elliptic curve
    points = ['infinity']
    for x in range(0,p):
        for y in range(0,p):
            if on_curve((x,y)):
                points.append((x,y))
    return points
                
def group_order():
    # Returns the order of the elliptic curve
    return len(points_on_curve())

def generators():
    # Returns the list of generators of the elliptic curve
    points = points_on_curve()
    group_order = len(points)
    generators = []
    for point in points:
        if order(point) == group_order:
            generators.append(point)
    return generators
