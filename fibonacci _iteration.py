import os

def fibonacci_iteration(n):
    if n < 3:
        return 1
    else:
        f1 = 1
        f2 = 1
        for i in range(3,n + 1):
            t = f1
            f1 = f2
            f2 = t + f1
        return f2

result = fibonacci_iteration(7)
print(result)
os.system('pause')
