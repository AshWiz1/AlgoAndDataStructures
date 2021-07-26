# Linear Diophantine Equation
def ext_gcd(a, b):  # a*x+b*y == gcd(a,b)  ==> return gcd(a,b),x,y
    if b > 0:
        d,x,y = ext_gcd(b,a % b)
        return d,y,x-(a//b)*y
    return a,1,0