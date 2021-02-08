import os

def multiplication_table():
    j = 1
    for i in range(1,10):
        for j in range(1,i + 1):
            print("%d * %d = %2d    "%(j,i,j*i),end="")
        print("\n")


multiplication_table()
os.system('pause')
