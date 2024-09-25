# Import the random module to enable random selection
import random

# Define a list of words to choose from
word_list = ["aardvark", "baboon", "camel"]

# Randomly select a word from the word_list
chosen_word = random.choice(word_list)

# Print the chosen word (for testing purposes)
print(chosen_word)

# Prompt the user to input a letter and store it in the variable 'guess'
guess = input("Diga uma letra:\n")
# Convert the user's input to lowercase to ensure case insensitivity
guess = guess.lower()

# Iterate over each letter in the chosen word
for letter in chosen_word:
    # Check if the current letter matches the user's guess
    if letter == guess:
        print("Right")  # If it matches, print "Right"
    else:
        print("Wrong")  # If it does not match, print "Wrong"
