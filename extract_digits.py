import os

def extract_digits():
    number = input("please input a number: ")

    digits_list = []
    lenth = len(number)
    number = int(number)
    for i in range(0,lenth):
        digits_list.append(number % 10)
        number = number/10
        print("the %d digit is: %d"%(i+1,digits_list[i]))


extract_digits()
os.system('pause')
