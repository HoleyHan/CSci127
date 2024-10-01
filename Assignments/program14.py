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

n = [] #creates an empty list

while len(n) < 5: # while the length of the list is less than 5
    degree=int(input("Please enter a number: "))
    n.append(degree) #adds the number to the list
    t.left(degree) #turns the turtle left the degrees entered
    t.forward(100) #moves the turtle forward 100

wn.exitonclick()