import math


def calc_paint(height, width, coverage):
    area = height*width/coverage
    cans = math.ceil(area)
    print(f"You'll need {cans} cans of paint ")


t_height = int(input("What is the wall height?: "))
t_width = int(input("What is the wall width?: "))

covarage = 5

calc_paint(height=t_height, width=t_width, coverage=covarage)