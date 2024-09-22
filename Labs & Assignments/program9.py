#Name: Han Ning Zhang, Han Zhang
#Email: han.zhang65@myhunter.cuny.edu, han.zhang.med18@gmail.com
#Date: September 22, 2024
#Create hex-color input turtle coloring program
import turtle

#Write a program that asks the user for the hexcode of a color and then displays a turtle that #color.
myTurtle = turtle.Turtle()

colorInput = input("Enter a hex string: ") #user input includes #
#hexString = "#" + hexString

myTurtle.shape("turtle")
myTurtle.color(colorInput)
#A sample run of your program should look like:

#Enter a hex string:  #A922A9
#and the output should look similar to: (purple turtle)
