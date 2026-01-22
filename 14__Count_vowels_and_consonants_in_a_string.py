'''
  ALGORITHM

1. Take a string from the user
2. Convert it to lowercase (to handle 'A' and 'a' equally)
3. Traverse each character one by one
4. Check:
        If character is a letter
        If it is one of the vowels → a, e, i, o, u
5. Increase:
        Vowel count (or)
        Consonant count
6. Ignore spaces, digits, and symbols

'''


# Example

word = " hello world"
# vowels = {e,o,o} -> 3
# consonants = {h,l,l,w,r,l,d} -> 7



# Implementation 
def count_vowels_consonants(s: str) -> tuple:
    s = s.lower()
    vowels = 0
    consonants = 0
    
    for char in s:
        if (char >= 'a' and char <= 'z'):
            if char in ['a','e','i','o','u']:
                vowels += 1
            else:
                consonants += 1
    return (vowels,consonants)

string = input("Enter the string: ")
v, c = count_vowels_consonants(string)
print("Vowels Count: ",v)
print("Consonant Count: ",c)
    
    

# Time Complexity : O(n)
# (n characters in the string taken out one by one till the end)
# Space Complexity: O(1)
# (maximum we stored single value in a variable)
