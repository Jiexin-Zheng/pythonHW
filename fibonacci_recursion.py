import os

def fibonacci_recursion(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)

result = fibonacci_recursion(7)
print(result)
os.system('pause')
