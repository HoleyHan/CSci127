#Name: Han Ning Zhang, Han Zhang
#Email: han.zhang65@myhunter.cuny.edu, han.zhang.med18@gmail.com
#Date: September 17, 2024
#Lecture Slip 1

#Write a Python program that:
#Asks the user to enter their first name.
#Gets the length of the name entered and stores that value in a variable.
#Using the turtle library, draws a polygon where the number of sides equals the length of the user's name.
import turtle

wn=turtle.Screen()

firstNameTurtle=turtle.Turtle()
firstName = input("Please enter your first name: ")

firstNameLength = len(firstName)

turtle.forward(firstNameLength * 100)
turtle.left(360 / firstNameLength)
#Turtle module GUI

#Move hanZ to form an octagon, move forward 100 steps, then turn is about 45 degree, repeat for 8 the 8 sides:

#for i in range(8):
#	hanZ.forward(100)
#	hanZ.left(45) #45 degrees

wn.exitonclick()