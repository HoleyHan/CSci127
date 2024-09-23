#Name: Han Ning Zhang, Han Zhang
#Email: han.zhang65@myhunter.cuny.edu, han.zhang.med18@gmail.com
#Date: September 22, 2024
#Create hex-color input turtle coloring program
import turtle

wn=turtle.Screen()

t = turtle.Turtle()

hexString = input("Enter a hex string: ") #user input includes #
t.shape('turtle')
t.color(hexString) 

turtle.exitonclick()

