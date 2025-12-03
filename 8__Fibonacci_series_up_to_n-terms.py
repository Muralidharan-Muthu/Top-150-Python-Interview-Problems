# Fibonacci series up to n terms


""" 
initial values - 0,1

terms -> 8

[0,1,1,2,3,5,8,13]

0 + 1 = 1
    1 + 1 = 2
        1 + 2 = 3
            2 + 3 = 5
                3 + 5 = 8
                    5 + 8 = 13


"""

def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0,1]
    while(len(seq) < n):
        seq.append(seq[-1] + seq[-2])
    return seq

n = int(input("Enter the terms : "))
print("Fibonacci Series: ",fibonacci(n))


