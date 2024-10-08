#Name: Han Ning Zhang, Han Zhang
#Email: han.zhang65@myhunter.cuny.edu, han.zhang.med18@gmail.com
#Date: October 8, 2024
#Create cypher encrypting program


#Write a program that prompts the user to enter a word and then prints out the word with each #letter shifted right by 13. 
#That is, 'a' becomes 'n', 'b' becomes 'o', ... 'y' becomes 'l', and #'z' becomes 'm'. Assume that all inputted words are in lower case letters: 'a',...,'z'.

# Define the alphabet string
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_length = len(alphabet)

# Function to perform the encoding
def f(word):
    encoded_word = ""
    for char in word:
        if char in alphabet:  # Ensure the character is a lowercase letter
            index = alphabet.index(char)  # Find the index of the character in the alphabet
            new_index = (index + 13) % alphabet_length  # Calculate the new index with wrap-around
            encoded_word += alphabet[new_index]  # Find the new character from the alphabet
        else:
            encoded_word += char  # Append unchanged characters
    return encoded_word

# Prompt the user for input
word = input("Enter a word: ").strip()  # Get user input and strip whitespace

encoded_word = f(word)  # Call the function with the new word
print("Your word in code is:\n", encoded_word)  # Output the shifted word