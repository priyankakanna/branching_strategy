# factorial.py
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("Factorial of 5:", factorial(5))
# Make changes to factorial.py
# Test, fix bugs, and prepare for release