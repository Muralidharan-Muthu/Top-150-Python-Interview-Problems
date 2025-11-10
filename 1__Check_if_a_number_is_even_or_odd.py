
# 1. Check if a number is even or odd

num = int(input("Enter a number : "))

def evenOrOdd(num: int) -> str:
    if(num % 2 == 1):
        return "Odd"
    else:
        return "Even"

print(f"The number {num} is ",evenOrOdd(num))



