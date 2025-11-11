# Find largest of three numbers

a = 70
b = 20
c = 30

def largestOfThree(a:int,b:int,c:int) -> int:
    if(a > b and a > c):
        return a
    elif(b > a and b > c):
        return b
    else:
        return c
    
print(" The Largest of three numbers : ",largestOfThree(a,b,c))
