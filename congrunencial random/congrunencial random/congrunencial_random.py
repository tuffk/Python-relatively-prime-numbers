def gdc(x,y):
    t =0
    while (y != 0):
        t = x
        x = y 
        y = t % y
    return x;

def relativePrime( x,y):
    z = gdc(x,y)
    if z == 1:
        return True
    else:
        return False

a = int(input("a="))
b = int(input("b="))
print( relativePrime(a,b))