import turtle

# Turtle module GUI
wn = turtle.Screen()
t = turtle.Turtle()

# Ask the user for 5 angles and move the turtle accordingly
for i in range(5):
    while True:  # Keep asking until valid input is entered
        try:
            degree = int(input("Please enter an integer degree: "))
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    t.left(degree)  # Turn the turtle left by the entered degrees
    t.forward(100)  # Move the turtle forward by 100 units

wn.exitonclick()  # Exit when the window is clicked
wn.mainloop()  # Keep the turtle window open