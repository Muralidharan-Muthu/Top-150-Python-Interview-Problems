# find factorial of the number

def factorial(num : int) -> int:
    if (num <= 2) : return num

    fact = 1
    while(num > 0):
        fact = fact * num
        num = num - 1
    return fact
num = int(input("Enter the number: "))
print(f"The Factorial of {num} is ",factorial(num))


""" 
factorial

5! => 5 x 4 x 3 x 2 x 1 = 120
4! => 4 x 3 x 2 x 1 = 24
...
1! => 1
0! => 1

"""


