from turtle import *
import colorsys
speed(0)
h=0.0
bgcolor('black')
pensize(2)

for i in range(150):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.105
    circle(4-i,150)
    lt(80)
    circle(4-i,150)
    rt(100)

done()