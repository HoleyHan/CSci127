#Name: Han Ning Zhang, Han Zhang
#Email: han.zhang65@myhunter.cuny.edu, han.zhang.med18@gmail.com
#Date: September 3, 2024
#This program draws 5-pointed star

#Import Turtle module
import turtle

#Turtle module GUI
wn=turtle.Screen()

#Instantiating a turtle named: hanZ
hanZ = turtle.Turtle()

#For the 5-pointed star, the turtle turns 2 complete revolutions (720 degrees).
#How much does the turtle need to turn at each point? 720/5 = 144

for i in range(5):
  hanZ.left(144)
  hanZ.forward(100)

wn.exitonclick()
