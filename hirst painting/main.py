# import colorgram
"""installed colorgram package to extract colors from any image"""
# #import images.jpg
# color_rgb=[]
# colors=colorgram.extract("images.jpg",25)
# for i in colors:
#     r=i.rgb.r
#     g=i.rgb.g
#     b=i.rgb.b
#     new_tuple=(r,g,b)
#     color_rgb.append(new_tuple)
# print(color_rgb)
from turtle import *

from turtle import *
from random import choice


color_list=[(235, 231, 223), (165, 164, 159), (243, 231, 236), (227, 239, 230), (226, 231, 239), (146, 161, 153), (148, 98, 63), (223, 210, 96), (154, 14, 34), (186, 151, 163), (133, 163, 196), (194, 158, 26), (57, 91, 155), (21, 40, 68), (129, 68, 94), (38, 29, 20), (80, 14, 50), (32, 50, 42), (162, 16, 8), (227, 169, 190), (195, 94, 141), (16, 54, 125), (161, 215, 197), (66, 95, 79), (185, 185, 211)]


rumi=Turtle()
screen=Screen()
screen.colormode(255)
rumi.speed(0)
rumi.hideturtle()

def shift():
    for i in range (10):
        rumi.dot(20,choice(color_list))
        rumi.penup()
        rumi.forward(50)
y=0

for i in range(1,11):
    shift()
    y+=40
    rumi.setpos(0,y)
    #shift()
    #rumi.setpos(0,y)


screen.exitonclick()