import os

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def calculator1():
    print("please choose your operation")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    choice = input("please input your choice  ")
    num1 = float(input("please input your left number  "))
    num2 = float(input("please input your right number  "))
    if choice == '1':
        print(num1,"+",num2,"=",add(num1,num2))
    elif choice == "2":
        print(num1,"-",num2,"=",subtract(num1,num2))
    elif choice == "3":
        print(num1,"*",num2,"=",multiply(num1,num2))
    elif choice == "4":
        print(num1,"/",num2,"=",divide(num1,num2))
    else:
        print("invalid input!!")

calculator1()
os.system('system')