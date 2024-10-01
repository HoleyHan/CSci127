#Name: Han Ning Zhang, Han Zhang
#Email: han.zhang65@myhunter.cuny.edu, han.zhang.med18@gmail.com
#Date: Oct 1, 2024
#Program14

import turtle

# Turtle module GUI
#wn = turtle.Screen()
t = turtle.Turtle()
#t.speed(5)

# Ask the user for 5 angles and move the turtle accordingly
for _ in range(5):  # Loop 5 times
    degree = int(input("Please enter an integer degree: "))
    t.left(degree)  # Turn the turtle left by the entered degrees
    t.fd(100)  # Move the turtle forward by 100 units

#wn.exitonclick()  # Exit when the window is clicked

#test 270, 100, 190, 200, 80