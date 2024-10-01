#Name: Han Ning Zhang, Han Zhang
#Email: han.zhang65@myhunter.cuny.edu, han.zhang.med18@gmail.com
#Date: September 24, 2024
#Moving program

import turtle				

turtle.colormode(255)		#Allows colors to be given as 0...255
t = turtle.Turtle()		
t.shape("turtle")		#Make it turtle shaped
t.backward(100)			#Move her backwards, to give more space to draw

#For 0,10,20,...,250
for i in range(0,255,10):
     t.forward(10)		#Move forward
     t.pensize(i)		#Set the drawing size to be i (larger each time)
     t.color(0, 0, i)		#RGB Set the blue channel to be i (brighter each time)