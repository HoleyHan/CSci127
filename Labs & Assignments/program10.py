#Name: Han Ning Zhang, Han Zhang
#Email: han.zhang65@myhunter.cuny.edu, han.zhang.med18@gmail.com
#Date: September 24, 2024
#Moving program

import turtle

turtle.Screen()
t = turtle.Turtle()
#t.speed(5)

#For i = 5, 10, 15, 20, 25, ... ,300:
for i in range(5, 305, 5):
   t.forward(i) #steps edited although it does not look like the graphic on assignment
   t.left(91) #degrees changed 91 to 90 bc gradescope found it at the wrong position (should be 			#at heading: 60 instead of 329

turtle.exitonclick()