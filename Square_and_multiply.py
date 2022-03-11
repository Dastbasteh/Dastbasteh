#################################### Square and multiply algorithm computes x^y mod n ########################
    
def SAM(x,y,n):
    def binary(n):
      return bin(n).replace("0b", "")
    y=binary(y)
    z=1
    for char in y:
        if char=="1":
            z=((z**2)*x)%n
        else:
            z=(z**2)% n
    return(z)
print(SAM(2**100,3**50,5**70))
# compare it with the usuall computation (may take a long time):
print(((2**100)**(3**50)) %(5**70)) 
