from turtle import *
import colorsys
tracer(20)
h=0
bgcolor('black')

for i in range(150):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    begin_fill()
    forward(i)
    left(10)
    backward(i*1.5)
    circle(i*0.5,280)
    end_fill()
    h+=2.049
done()