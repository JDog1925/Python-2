#Implement a recursive function to calculate the factorial of a non-negative integer.
#Instructions:
#Write a recursive function    factorial(n) that returns the factorial of the non-negative integer    n.
#The factorial of    n (denoted as    n!) is defined as:
#n! = n * (n-1)! for n > 0
#0! = 1
#Write test cases to verify the function works correctly for different values of    n.

def factorial(n):
    # base case! Factorial of 0 then it should be 1
    if n == 0:
        return 1
    #recursive case! n * factorail of (n - 1)
    else:
        return n * factorial(n -1)

result = factorial(4)
print("Factorial of 4 is: ", result)
result = factorial(5)
print("Factorial of 5 is: ", result)