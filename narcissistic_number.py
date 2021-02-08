import os

def narcissistic_number():
    for i in range(100, 1000):
        hundreds_digit = i // 100
        tens_digit = i % 100 // 10
        units_digit = i % 10
        if i == hundreds_digit ** 3 + tens_digit ** 3 + units_digit ** 3:
            print(i)

narcissistic_number()
os.system('pause')