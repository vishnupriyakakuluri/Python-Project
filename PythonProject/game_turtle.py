#Turtle race
import time
import turtle
from turtle import Turtle
from random import randint

#background
window=turtle.Screen()
window.title("Race")
turtle.bgcolor("palegreen")
turtle.penup()
turtle.setpos(-75,300)
turtle.penup()
turtle.write("Race", font=("Ariel",30,"bold"))

#finish line
st=20
sq=15
fl=400
turtle.color("black")
turtle.shape("square")
turtle.shapesize(sq/st)
turtle.penup()

for i in range(10):
    turtle.setpos(fl,(100-(i*sq*2)))
    turtle.stamp()

for j in range(10):
    turtle.setpos(fl+sq,((100-sq)-(j*sq*2)))
    turtle.stamp()

turtle.hideturtle()

#Turtles
turtle1=Turtle()
turtle1.speed(0)
turtle1.color("pink")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-350,60)
turtle1.pendown()

turtle2=Turtle()
turtle2.speed(0)
turtle2.color("yellow")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-350,-10)
turtle2.pendown()

turtle3=Turtle()
turtle3.speed(0)
turtle3.color("black")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-350,-80)
turtle3.pendown()

time.sleep(1)

#move
for i in range(245):
    turtle1.forward(randint(1,15))
    turtle2.forward(randint(1,5))
    turtle3.forward(randint(1,5))

turtle.exitonclick()








