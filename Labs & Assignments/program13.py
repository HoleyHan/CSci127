#Name: Han Ning Zhang, Han Zhang
#Email: han.zhang65@myhunter.cuny.edu, han.zhang.med18@gmail.com
#Date: September 24, 2024
#Program13

#Program 13: Asks for a message, then prints the message in reverse with two copies for each character per line.

m = input("Enter a message: ")

lastIdn = len(m)-1 #total count - 1
for i in range(lastIdn,-1,-1): #starts at last char, stops at last char, goes in reverse.
    print(m[i],m[i])