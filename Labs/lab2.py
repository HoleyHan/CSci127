#Name: 
#Email: 
#Date: September 10, 2024
#Lab 2

#Strings,  a sequence of characters, are indicated by '' or "".
#Strings, string methods, string indexing, get user input, loop through strings, for and range() function, loop through lists, split() function, command line, and learn unix commands.

#strings start off at index 0 e.g.

greeting="Hello, World!"

print(greeting[0]) #prints the first character

#Particular string methods: upper() and lower(), len(), count(), find(), split(), join(), strip(), replace()
#String slicing methods obtain a substring.

#print(greeting.upper()) #converts to uppercase
#print(greeting.lower()) #converts to lowercase
#print(len(greeting)) #counts the number of characters vs count which counts the number of a specific value appears in the string
#print(greeting.count('o')) #counts the number of 'o'
#print(greeting.find(' ')) #counts any blank spaces
#print(greeting.find('ll')) #counts the number of l's

#print(greeting.split(",")) #splits the string at the comma
#print(greeting.join("a")) #joins the string with a character 

#print(greeting.strip()) #removes any leading or trailing spaces, we can also add a specific character to remove
#print(greeting.strip("o")) #removes the letter H
#print(greeting.strip('')) #removes the spaces

#print(greeting.replace("H", "h")) #replaces the letter H with h

#mess = input('Please enter a message to show user: ')  #user input
#print("You entered", mess)  #outputs user input via a string variable

#loops through strings are lists in python
#for i in greeting: #loops through the string greeting one character at a time
#    print(i) #prints each character on a new line

#ASCII table interpretation methods
#chr(character) returns a character represented by a unicode number
#ord(number) returns a number represented by a unicode number of a specified character
#hex(number) returns a hexidecimal number of a specified number base 16 instead of base 10

n=0 #initialize counter variable outside the loop to 0
for i in range(97, 123): # starts at 97 which is the ascii value of 'a', 122 is the ascii value of 'z' but we set it to 123 to stop the loop at 122.
    #range(start, stop, step) start and step are optional and stop is required.
    n = n+1 #adds 1 to the counter variable n every time the loop runs
    print(n, chr(i), ord(chr(i))) #prints the counter variable n, the ascii value of the character, the character, and the ascii value of the character

#print(greeting.split("l")) #splits the string at the l

#Indexing a string
#string[start:stop:step]

#Types of variables in python are integers, floats, strings
# Strings are indexed from 0 to n-1

#Integers are used to store whole numbers
#Len(int) cannot be used to find the length of an integer because they don't have length

#Lists are used to store multiple values in a single variable
#Lists are indicated by [0, 1, 2,..., n] where n is the number of elements in the list
#Lists are mutable, can be indexed, sliced, appended, mutipled in the same way as strings 

#Lists can be created using the list() function
#Lists can be created using the range() function

#List methods: append(), insert(), remove(), sort(), clear(), reverse(), copy()

#List concatenation and replication
#List concatenation is done with the + operator to combine two lists
#List replication is done with the * operator to repeat a list

#Tuples are used to store multiple values in a single variable using () 
#Tuples are indicated by (0, 1, 2,..., n) where n is the number of elements in the tuple
#Tuples are immutable, can be indexed, sliced, appended, mutipled in the same way as strings

#Tuples can be created using the tuple() function
#Tuple methods are count(), index() 

#Sets are used to store multiple values in a single variable using {}
#Sets are indicated by {0, 1, 2,..., n} where n is the number of elements in the set
#Sets are mutable, can be indexed, sliced, appended, mutipled in the same way as strings

#Sets can be created using the set() function
#Set methods are add(), remove(), clear(), copy() 

#Dictionaries are used to store multiple values in a single variable using pairs enclosed by brackets {}
#Dictionaries are indicated by {key: value, key: value, key: value, ...} where the keys are unique and the values are not
#Dictionaries are mutable, can be indexed, sliced, appended, mutipled in the same way as strings

#Dictionaries can be created using the dict() function
#Dictionary methods: clear(), copy(), fromkeys(), get(), items(), keys(), pop(), popitem(), setdefault(), update(), values()


#Biomolecular Sequences Program Nucleotide counter and Chargarff calculator

#Initial fragment of insulin DNA (h. sapiens):
insulin = "AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGGGCCTTTGCGTCAGGTGGGCTCAGGATTCCAGGGTGGCTGGACCCCAGGCCCCAGCTCTGCAGCAGGGAGGACGTGGCTGGGCTCGTGAAGCATGTGGGGGTGAGCCCAGGGGCCCCAAGGCAGGGCACCTGGCCTTCAGCCTGCCTCAGCCCTGC"

#Compute the length, and store in variable to use again:
l = len(insulin)
print("The length is", l)

#Compute amount of C and G in the sequence:
numC = insulin.count('C')
numG = insulin.count('G')
print('Number of C nucleotides', numC)
print('Number of G nucleotides', numG)

#Compute the GC-content:
gc = (numC + numG) / l
#Convert to percentage by multiplying by 100:
gcPercent = gc * 100
print('GC-content is', gcPercent)

#Chargaff's Rule:
at = (1-gc)
numA = (at/2)*100
numT = (at/2)*100
print('Number of A nucleotides', numA)
print('Number of T nucleotides', numT)

#Acronyms

#Based on the programs demoed above, combine the use of split() and indexing (the use of square #brackets to access individual characters in a string using the character's index) to write a #program that takes a phrase and creates an acronym of the phrase: that is, the first letter of #each word.

#1. Prompt for a phrase & read it in.
#2. Make the phrase upper case.
#3. Split up the phrase into words.
#4. Take the first letter of each word (keep in mind that split() returns a list of the words ), concatenate and make an #acronym of it

#e.g. Enter a phrase:  City University New York
#Your phrase in capital letters:  CITY UNIVERSITY NEW YORK
#Acronym:  CUNY

phrase = input("Enter a phrase: ")
bigPhrase = phrase.upper()
print("Your phrase in capital letters:", bigPhrase)

wordList = bigPhrase.split() #split into words into a list
acronym = ""  #Initialize as a string

for word in wordList:
    letter = word[0]
    acronym += letter  # +=Concatenate each letter to the acronym string

print("Acronym:", acronym)


