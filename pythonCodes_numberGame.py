# Before we start: import modules
import random

# Write a function that generates a random number between 0 and 5000
def generateNumber():
    goal = random.randint(0, 5000)
    return goal

# Write a function that checks whether the entered number is bigger or smaller than the target number, and tells this to the user.
def analyseInput(entered, goal):
    if entered>goal:
        print("Too big")
    else :
        print("Too small")

# Call the first function to generate a secret number. Our goal is to guess this number.
goal = generateNumber()

# Ask the user to enter a guess and store the guess in a variable.
entered = int(input("Enter your guess\n"))

# Add some code that repeatedly calls the second function as long as the user's choice does not match the correct number.
# That way, the user can keep guessing until they found the number.
# Once it is found, print a victory message.
# Hint: You can use a WHILE-loop for this
while(entered!=goal):
    analyseInput(entered, goal)
    entered = int(input())
print("CONGRATS")
