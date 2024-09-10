#Name: Han Ning Zhang, Han Zhang
#Email: han.zhang65@myhunter.cuny.edu, han.zhang.med18@gmail.com
#Date: September 9, 2024
#ASCII output program


#create ASCII dictionary.

# Create the ASCII dictionary
ascii_dict = {chr(i): i for i in range(32, 127)}

# Print the ASCII dictionary
print("ASCII Dictionary:")
print(f"{'Character':<10} {'Decimal Value':<15}")
print("-" * 25)

for char, value in ascii_dict.items():
    print(f"{char:<10} {value:<15}")

x = input("Enter a phrase: ")

print("In ASCII: ")

a=x.upper()
b=x.casefold()


print(a)
print(b)

