from turtle import*
bgcolor("black")
speed(0)
hideturtle()
pensize(6)
for i in range(200):
    for j in range(4):
        color("hot pink")
        fd(0.2*i*j)
        left(91)
    left(73*15/100+15)
done()