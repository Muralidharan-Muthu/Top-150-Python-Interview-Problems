# Approach

"""
1. A prime number is a number greater than 1

2. It has only two divisors → 1 and itself

3. To check primality efficiently:
   Check divisibility only up to √n
   example: n = 36
            √n = 6 
            
            1 x 36 -> 36
            2 x 18 -> 36
            3 x 12 -> 36
            4 x 9  -> 36
            6 x 6  -> 36
            
            9 x 4  -> 36
            12 x 3 -> 36
            18 x 2 -> 36
            36 x 1 -> 36
            
   
   If divisible → not prime

1/2 -> 0.5 


Time Complexity -> O(n √n)
Space Complexity -> O(1) 

"""




def print_primes(start,end):
    for num in range(start,end+1):
        if num < 2:
            continue
        
        is_prime = True
        
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            print(num, end=" ")

start = int(input("Enter the start: "))
end = int(input("Enter the end: "))
print("Printing the prime numbers")
print_primes(start,end)    
    