#Name: Han Ning Zhang, Han Zhang
#Email: han.zhang65@myhunter.cuny.edu, han.zhang.med18@gmail.com
#Date: September 24, 2024
#Turtle pentagon moving program

import turtle
wn=turtle.Screen()

t = turtle.Turtle()

#pentagon 360/5 = 72 degrees
#t.speed(10)

t.shape("turtle")
t.color("cornflowerblue") #keep casing consistent

for i in range(5):
    t.stamp()
    t.fd(100) # steps
    t.lt(72) # degrees

wn.exitonclick()