####################### Extended Euclidean algorithm(a,b) and multiplicative inverse of a mod b ############################################
#It takes a,b and returns gcd(a,b) and sa+tb=r, here a>=b
def Extended_Euclidean(a,b):
    a0=a
    b0=b
    t0=0
    t=1
    s0=1
    s=0
    q=a0//b0
    r=a0-q*b
    while r>0:
        temp=t0-q*t
        t0=t
        t=temp
        temp=s0-q*s
        s0=s
        s=temp
        a0=b0
        b0=r
        q=a0//b0
        r=a0-q*b0
    r=b0
    return [r,s,t]
print(Extended_Euclidean(2**100,(2**101)+2))
##########################Inverse of a mod b ############################
def Multiplicative_inverse(a,b):
    return((Extended_Euclidean(a,b)[1])%b)
print(Multiplicative_inverse(2**100,(2**101)+1))
