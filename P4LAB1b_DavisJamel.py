#CTI-110
#P4LAB1b 
#Jamel Davis
#March 29, 2023

import turtle
wn = turtle.Screen()
wn.bgcolor("white")

tur = turtle.Turtle()
tur.color("black")
tur.pensize(5)

tur2 = turtle.Turtle()
tur2.color("black")
tur2.pensize(5)

tur.penup()
tur.goto(0, 80)
tur.pendown()
tur.setheading(270)
tur.forward(130)
tur.circle(-50, 180)
tur.hideturtle()

tur2.penup()
tur2.goto(50, -100)
tur2.pendown()
tur2.setheading(90)
tur2.forward(180)
tur2.setheading(360)
tur2.circle(-90, 180)
tur2.hideturtle()

turtle.done()




