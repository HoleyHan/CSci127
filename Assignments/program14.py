#Name: Han Ning Zhang, Han Zhang
#Email: han.zhang65@myhunter.cuny.edu, han.zhang.med18@gmail.com
#Date: Oct 1, 2024
#Program14: Write a program that asks the user for 5 whole (integer) numbers. 
#For each number, turn the turtle left the degrees entered and then the turtle should move forward 100.

#Program 13: Asks for a message, then prints the message in reverse with two copies for each character per line.

import turtle

#Turtle module GUI
wn = turtle.Screen()

t=turtle.Turtle()

#For each number, turn the turtle left the degrees entered and then the turtle should move forward 100.

for i in range(5):
    t.left(int(input("Enter a number: ")))
    t.forward(100)

wn.exitonclick()