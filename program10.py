#Name: Han Ning Zhang, Han Zhang
#Email: han.zhang65@myhunter.cuny.edu, han.zhang.med18@gmail.com
#Date: September 20, 2024
#Moving program

#Write a program that implements the pseudocode below:
#For i = 5, 10, 15, 20, 25, ... ,300:
#Walk forward i steps
#Turn left 91 degrees
#Your output should look similar to:
#Hint: See examples of range(start,stop,step) in lecture 2

n = 0 #counter
for i in range(5,301,5):
	n +=1
	print(n, f"Walk forward {i} steps")
	print("Turn left 91 degrees")
