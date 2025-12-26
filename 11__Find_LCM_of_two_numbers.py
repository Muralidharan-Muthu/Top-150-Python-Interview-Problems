
# LCM Of Two NUmbers

# LCM - Least Common Multiple

def LCM(a:int,b:int) -> int:
    if (a > b):
        largest = a
        smallest = b
    else:
        largest = b
        smallest = a
    # 6 , 4 -> 6*4 => 24
    for i in range(largest,a*b+1,largest):
        if (i%smallest == 0):
            return i
    return a*b

a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))
print(f"LCM of {a} and {b} is {LCM(a,b)}")












"""
a -> 5
b -> 10

 5      15     25        35...
    10      20      30 ...
    
    
    
    
    
    
    

worst case 

a -> 7 (prime number)
b -> 13 (prime number)

LCM -> a*b = 91

"""












""" 
Example: LCM(6,4)
largest -> 6, smallest -> 4
6   4  -> 6%4 = 2
12  4  -> 12%4 = 0

LCM -> 12

"""
