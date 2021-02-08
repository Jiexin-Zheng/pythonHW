import os

def triangle_judge():
    segment1 = float(input("please input the first segment: "))
    segment2 = float(input("please input the second segment: "))
    segment3 = float(input("please input the third segment: "))
    flag_right = 0
    flag_equilateral = 0
    flag_lsosceles = 0
    sum1 = segment1 + segment2
    sum2 = segment1 + segment3
    sum3 = segment2 + segment3
    if(sum1 > segment3 and sum2 > segment2 and sum3 > segment1):
        square1 = segment1 ** 2
        square2 = segment2 ** 2
        square3 = segment3 ** 2
        if((square1 == square2 + square3) or (square2 == square1 + square3) or (square3 == square2 + square1)):
            flag_right = 1
        if((segment2 == segment3) or (segment1 == segment3) or (segment1 == segment2)):
            flag_lsosceles = 1
            if((segment1 == segment2) and (segment1 == segment3) and (segment2 == segment3)):
                flag_equilateral = 1
    else:
        print("the segments you input can not construct a triangle")

    if(flag_right == True):
        print("the segments you input can construct a right triangle")
    elif(flag_equilateral == True):
        print("the segments you input can construct an equilateral triangle")
    elif(flag_lsosceles == True):
        print("the segments you input can construct a lsosceles triangle")
    else:
        pass


triangle_judge()
os.system('pause')