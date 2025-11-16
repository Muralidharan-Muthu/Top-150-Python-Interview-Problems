# Reverse a number

def reverseNumber(num: int) -> int:
    reverse = 0
    while(num > 0):
        lastDigit = num % 10 # last digit 
        reverse = reverse * 10 + lastDigit
        num = num // 10
    return reverse

num = int(input("Enter the number: "))
print("Reversed number: ",reverseNumber(num))


