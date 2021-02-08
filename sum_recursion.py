import os

def sum_recursion(n):
    if n > 1:
        return n + sum_recursion(n - 1)
    else:
        return 1

sum1 = sum_recursion(100)
print(sum1)
os.system('pause')