from turtle import *
speed(0)
width(3)
#square
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#door
forward(60)
color("red")
begin_fill()
left(90)
forward(100)
right(90)
forward(70)
right(90)
forward(100)
end_fill()
#roof
penup()
goto(200,200)
pendown()
color("green")
begin_fill()
right(135)
forward(150)
left(93)
forward(144)
end_fill()
#window
penup()
goto(25,140)
pendown()
color("blue")
begin_fill()
right(138)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
penup()
goto(175,140)
pendown()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

exitonclick()
