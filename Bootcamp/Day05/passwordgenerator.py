import random  # Import the random module to use its functions

# Lists of characters to be used in the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")  # Welcome message

# User inputs for the number of letters, symbols, and numbers in the password
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_list = []  # Initialize an empty list to store the password characters

# Add random letters to the password list
for char in range(nr_letters):
    password_list.append(random.choice(letters))

# Add random symbols to the password list
for char in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Add random numbers to the password list
for char in range(nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)  # Shuffle the list to mix letters, symbols, and numbers
password = ''.join(password_list)  # Convert the list to a string

print(f"Your generated password is: {password}")  # Print the final password
