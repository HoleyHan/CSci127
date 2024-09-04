#Name: Han Ning Zhang, Han Zhang
#Email: han.zhang65@myhunter.cuny.edu, han.zhang.med18@gmail.com
#Date: September 3, 2024
#This program draws an flower.

#Import Turtle module
import turtle

#Turtle module GUI
wn=turtle.Screen()

#Instantiating a turtle named: hanZ
hanZ = turtle.Turtle()

#set turtle speed to max 10
#hanZ.speed(10)

#Repeat 36 times: 
            #Walk forward 100 steps
            #Turn left 145 degrees 
            #Walk forward 10 steps 
            #Turn right 90 degrees 
            #Walk forward 10 steps 
            #Turn left 135 degrees 
    	    #Walk forward 100 steps

#each iteration completes one "petal" so we need 36 times

for i in range(36):
	hanZ.forward(100)
	hanZ.left(145) #45 degrees
	hanZ.forward(10)
	hanZ.right(90)
	hanZ.forward(10)
	hanZ.left(135)
	hanZ.forward(100)

wn.exitonclick()
