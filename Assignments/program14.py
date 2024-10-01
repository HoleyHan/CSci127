#Name: Han Ning Zhang, Han Zhang
#Email: han.zhang65@myhunter.cuny.edu, han.zhang.med18@gmail.com
#Date: Oct 1, 2024
#Program14

import turtle

# Turtle module GUI
#wn = turtle.Screen()
t = turtle.Turtle()
t.speed(5)

# Track the initial heading (should be 0)
#initial_heading = t.heading()
#print(f"Initial heading: {initial_heading}")

turnList2 = [72, 72, 72, 72, 72]
for n in turnList2:
  t.left(n)
  t.fd(100)
  t.write(t.heading())

turnList = [270, 100, 190, 200, 80]
for n in turnList:
  t.left(n)
  t.fd(100)
  t.write(t.heading())

# Ask the user for 5 angles and move the turtle accordingly
for _ in range(5):  # Loop 5 times
    degree = int(input("Please enter an integer degree: "))
    t.left(degree)  # Turn the turtle left by the entered degrees
    t.fd(100)  # Move the turtle forward by 100 units
    t.write(t.heading()) # Write the current heading

#wn.exitonclick()  # Exit when the window is clicked

#test 270, 100, 190, 200, 80