
# Find the sum of digits of the number

num = 3456
# 3 + 4 + 5 + 6 
# 18

def sumOfTheDigits(num:int) -> int:
    num = abs(num)
    total = 0
    while (num > 0):
        total += num % 10 # 3456 % 10 -> 6
        num //= 10 # 3456 // 10 -> 345
    return total

n = int(input("Enter the number: "))
print(f"Sum of the digits of the number {n} is ",sumOfTheDigits(n))