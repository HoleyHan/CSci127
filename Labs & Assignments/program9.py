#Name: Han Ning Zhang, Han Zhang
#Email: han.zhang65@myhunter.cuny.edu, han.zhang.med18@gmail.com
#Date: September 9, 2024
#Create cypher encrypting program


#Write a program that prompts the user to enter a word and then prints out the word with each #letter shifted right by 13. That is, 'a' becomes 'n', 'b' becomes 'o', ... 'y' becomes 'l', and #'z' becomes 'm'. Assume that all inputted words are in lower case letters: 'a',...,'z'.

alphabet = "abcdefghijklmnopqrstuvwxyz" # Define the alphabet string in a variable

word = input("Enter a word: ") # Prompt the user to enter a word

encodedWord = "" #initialize a new string variable

alphabet_length = len(alphabet) # Get the length of the alphabet string 26

# Iterate over each character in the input word
for char in word:
    if char in alphabet:  # Ensure the character is a lowercase letter
        index = alphabet.index(char) # Find the index of the character in the alphabet
        new_index = index + 13 # Calculate the new index by shifting right by 13

	# Wrap around by subtracting if new_index exceeds the length #of the alphabet
        if new_index >= alphabet_length:
            new_index -= alphabet_length
        
        # Find the new character from the alphabet
        encodedWord += alphabet[new_index]


# Output the shifted word
print("Your word in code is:", encodedWord)
