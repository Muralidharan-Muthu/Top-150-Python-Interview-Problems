# Check if a number is palindrome 

def isPalindrome(num:int) -> bool:
    if(num < 0):
        return False
    
    original = num # copy
    reverse = 0
    while(num > 0): #1234
        lastdigit = num % 10
        reverse = reverse * 10 + lastdigit
        num = num // 10
    
    return reverse == original # True # False

num = int(input("Enter the number: "))
if(isPalindrome(num)):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")
    