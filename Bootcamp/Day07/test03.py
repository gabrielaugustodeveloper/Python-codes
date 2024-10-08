import random  # Import the random module to use for selecting a random word

# List of words to choose from
word_list = ["aardvark", "baboon", "camel"]

# Randomly select a word from the word_list
chosen_word = random.choice(word_list)
print(chosen_word)  # Print the chosen word for debugging (can be removed later)

# Initialize a placeholder to represent the word with underscores
placeholder = ""
word_length = len(chosen_word)  # Get the length of the chosen word

# Create a placeholder string with underscores for each letter in the chosen word
for position in range(word_length):
    placeholder += "_"
print(placeholder)  # Print the initial placeholder

# Variable to track if the game is over
game_over = False
correct_letters = []  # List to keep track of correctly guessed letters

# Loop until the game is over
while not game_over:
    # Prompt the user to guess a letter and convert it to lowercase
    guess = input("Guess a letter: ").lower()

    display = ""  # Initialize an empty string to build the current display of the word

    # Iterate through each letter in the chosen word
    for letter in chosen_word:
        if letter == guess:  # If the guessed letter is in the word
            display += letter  # Add the guessed letter to the display
            correct_letters.append(guess)  # Record the correct guess
        elif letter in correct_letters:  # If the letter has been guessed correctly before
            display += letter  # Show the letter
        else:
            display += "_"  # Otherwise, show an underscore

    print(display)  # Display the current state of the guessed word

    # Check if there are no more underscores, meaning the word has been fully guessed
    if "_" not in display:
        game_over = True  # Set the game over flag to True
        print("You win.")  # Print a winning message
