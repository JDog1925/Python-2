#Implement a recursive function to compute the nth Fibonacci number.
#Instructions:
#Write a recursive function    fibonacci(n) that returns the nth Fibonacci number.
#The Fibonacci sequence is defined as:
#F(0) = 0
#F(1) = 1
#F(n) = F(n-1) + F(n-2) for n > 1
#Write test cases to verify the function works correctly for different values of    n.

# create a function for calcultiong Fibonacci
def fibonacci(n):
    # base case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recusrive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(9))