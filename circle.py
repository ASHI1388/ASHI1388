from turtle import *
import colorsys
tracer(2)
speed(2)
h=0.7
bgcolor('black')
pensize(2)
setheading(80)

for i in range(150):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.008
    fd(i)
    rt(4)
    rt(50)
    fd(200)
    rt(120)

done()