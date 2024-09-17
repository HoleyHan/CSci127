#Name: Han Ning Zhang, Han Zhang
#Email: han.zhang65@myhunter.cuny.edu, han.zhang.med18@gmail.com
#Date: September 15, 2024
#ASCII interpretor program

#Write a program that prompts the user to enter a phrase and then prints out the ASCII
#code of each character in the phrase.

# Strings are immutable = cannot change existing strings but can add.


phrase = input("Enter a phrase: ")

word_list = phrase.split() # Split the phrase into word list

print("In ASCII:")
# Iterate over each word
for word in word_list:
    # Iterate over each character in the word
    for char in word:
        print(ord(char))