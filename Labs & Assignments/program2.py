#Name: Han Ning Zhang, Han Zhang
#Email: han.zhang65@myhunter.cuny.edu, han.zhang.med18@gmail.com
#Date: September 3, 2024
#This program draws an octagon.

import turtle #turtle is a library.

wn=turtle.Screen() #Turtle module GUI

hanZ = turtle.Turtle() #Instantiating a turtle named: hanZ

#Move hanZ to form an octagon - move forward 100 steps, turn 45°, & repeat for 8 the 8 sides:

for i in range(8):
	hanZ.forward(100) #100 steps
	hanZ.left(45) #45 degrees (360/5)

wn.exitonclick() #click on GUI to exit