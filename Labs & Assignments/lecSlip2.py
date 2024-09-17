#Name: Han Ning Zhang, Han Zhang
#Email: han.zhang65@myhunter.cuny.edu, han.zhang.med18@gmail.com
#Date: September , 2024
#Lecture Slip 2

#Strings,  a sequence of characters, are indicated by '' or "".
#Strings, string methods, string indexing, get user input, loop through strings, for and range() function, loop through lists, split() function, command line, and learn unix commands.

#strings start off at index 0 e.g.


myString = input("Please enter a string: ")

stringList = myString.split() #split into words into a list

for x in stringList: #loops through the list
    for ch in x: #loops through each character in the string
        n = ord(ch) #ord() returns the unicode number of a character
        y = n + 1 #y = unicode number + 1
        z = chr(y) #z = character
        print(ch, y, z) #prints the character, unicode number +1 and its corresponding character

