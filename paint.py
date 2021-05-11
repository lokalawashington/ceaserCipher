import math

def paint_calc(heght,width,cover):
    area = heght * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint")


test_h = int(input("Height of the wall"))
test_w = int(input("Width of the wall"))

coverage = 5
paint_calc(heght=test_h,width=test_w,cover=coverage)