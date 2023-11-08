import turtle


turtle.colormode(255)
turtle.speed(0)
turtle.penup()

turtle.goto(-25,-25)

turtle.pendown()

count = 0
for i in range(228):
    tcount = 0
    tcount = tcount + 1
    count = count + 1
    turtle.color(1 + count , 255 - count, 255 )
    turtle.forward(50 + count)
    turtle.left(90 + tcount)

turtle.left(-1)
turtle.forward(240)
turtle.hideturtle()

turtle.exitonclick()
