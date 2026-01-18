
''' 
Algorithm 

1. Take a string from the user

2. Compare first character with last character

3. Move forward from the start and backward from the end

4. If any pair doesn’t match → Not a palindrome

5. If all characters match → Palindrome


Example:

Palindrome -> madam == madam

Not Palindrome -> python != nohtyp

-> Odd
        m a d a m
        0 1 2 3 4
-> Even
        n o o n
        0 1 2 3
        
'''

def is_palindrome(s: str) -> bool:
    s = s.lower()
    start = 0
    end = len(s)-1
    
    while(start < end):
        if s[start] != s[end]:
            return False
        
        start += 1
        end -= 1
    
    return True
        
string = input("Enter the string: ")

if(is_palindrome(string)):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
    


'''
Time Complexity ->  O(n) 
(each character is checked once)

Space Complexity -> O(1)
(no extra memory used)
'''