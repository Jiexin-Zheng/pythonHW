import os

def get_leap_year():
    start = input("please input the starting year:")
    end = input("please input the ending year:")
    leap_list = []
    start = int(start)
    end = int(end)
    for i in range(start,end):
        if i%4 == 0 and i%100 != 0:
            leap_list.append(i)
        else:
            pass
    for i in range(0,len(leap_list)):
        print("%d"%(leap_list[i]))

get_leap_year()
os.system('pause')
