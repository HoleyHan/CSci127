#Name: Han Ning Zhang, Han Zhang
#Email: han.zhang65@myhunter.cuny.edu, han.zhang.med18@gmail.com
#Date: September 10, 2024
#Lab 2

#Strings,  a sequence of characters, are indicated by '' or "".
#Strings, string methods, string indexing, get user input, loop through strings, for and range() function, loop through lists, split() function, command line, and learn unix commands.

#strings start off at index 0 e.g.

greeting="Hello, World!"

print(greeting[0]) #prints the first character

#Particular string methods: upper() and lower()

print(greeting.upper()) #converts to uppercase
print(greeting.lower()) #converts to lowercase
print(len(greeting)) #counts the number of characters vs count which counts the number of a specific value appears in the string
print(greeting.count('o')) #counts the number of 'o'
print(greeting.find(' ')) #counts any blank spaces
print(greeting.find('ll')) #counts the number of l's
print(greeting[0:5]) #prints the first 5 characters

print(greeting.split(",")) #splits the string at the comma
print(greeting.split("l")) #splits the string at the l
print(greeting.join("a")) #joins the string at the a


