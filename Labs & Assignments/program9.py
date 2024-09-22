#Name: Han Ning Zhang, Han Zhang
#Email: han.zhang65@myhunter.cuny.edu, han.zhang.med18@gmail.com
#Date: September 22, 2024
#Create hex-color input turtle coloring program
import turtle

#Write a program that asks the user for the hexcode of a color and then displays a turtle that #color.
myTurtle = turtle.Turtle()

hexString = input("Enter a hex string: ")


myTurtle.shape("turtle")
myTurtle.color(hexString)
#A sample run of your program should look like:

print("and the output should look similar to: ", hexString)

#Enter a hex string:  #A922A9
#and the output should look similar to: (purple turtle)
