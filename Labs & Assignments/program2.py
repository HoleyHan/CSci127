#Name: Han Ning Zhang, Han Zhang
#Email: han.zhang65@myhunter.cuny.edu, han.zhang.med18@gmail.com
#Date: September 3, 2024
#This program draws an octagon.

#Import Turtle module
import turtle

#Turtle module GUI
wn=turtle.Screen()

#Instantiating a turtle named: hanZ
hanZ = turtle.Turtle()

#Move hanZ to form an octagon, move forward 100 steps, then turn is about 45 degree, repeat for 8 the 8 sides:

for i in range(8):
	hanZ.forward(100)
	hanZ.left(45) #45 degrees

wn.exitonclick()