
# FACTORIAL 
# def factorial (n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# fact = int(input('Enter a Number to find its factorial: ' ))
# print('The Factorial of f{fact} is: ',factorial(fact))

# POWER OF TWO

# def isPowerOfTwo(n):
#     if n == 1:
#         return True
#     elif n%2 == 1:
#         return False
#     elif n <= 0:
#         return False
#     else:
#         return isPowerOfTwo(n // 2)


# n = int(input("Enter a Number: "))

# if isPowerOfTwo(n):
#     print(f"{n} is a power of two.")
# else:
#     print(f"{n} is not a power of two.")

# POWER OF THREE

# def isPowerOfThree(n):
#     if n == 1:
#         return True
#     elif n%3 == 1:
#         return False
#     elif n <= 0:
#         return False
#     else:
#         return isPowerOfThree(n // 3)


# n = int(input("Enter a Number: "))

# if isPowerOfThree(n):
#     print(f"{n} is a power of three.")
# else:
#     print(f"{n} is not a power of three.")
    
    
    
    
# POWER OF THREE
def isPowerOfFour(n, power=0):
    if n == 1:
        print(f"It is a power of 4 (4^{power}).")
        return True
    elif n % 4 != 0 or n <= 0:
        return False
    else:
        return isPowerOfFour(n // 4, power + 1)

n = int(input("Enter a Number: "))

if isPowerOfFour(n):
    print(f"{n} is a power of Four.")
else:
    print(f"{n} is not a power of Four.")
