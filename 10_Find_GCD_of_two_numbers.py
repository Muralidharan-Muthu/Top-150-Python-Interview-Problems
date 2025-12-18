
# Find the GCD of two numbers

a = int(input("Enter the number a : "))
b = int(input("Enter the number b : "))

def gcd(a,b):
    a = abs(a)
    b = abs(b)
    while(b != 0):
        a,b = b,a%b # 48 18
        # a = 18 b = 12
    return a

print(f"GCD of two numbers {a} and {b}: ",gcd(a,b))






"""
GCD -> Greatest Common Divisor 

Example: 

       2 | 48,18 -> commonly divide with 2
       3 | 24,9  -> commonly divide with 3
         | 8,3   -> we can't commonly divide this with any number

       2 x 3 = 6 

GCD(48,18) = 6
                   
GCD(48,18)

Dividend  Divisor  Remainder
   48    %  18   =   12
   18    %  12   =   6
   12    %  6    =   0 
   6     %  0
         GCD = 6

"""