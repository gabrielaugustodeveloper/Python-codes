import random

choice = int(input("What do you want? Type 1 for Rock, 2 for Paper or 3 for Scissors.\n"))
random_integer = random.randint(1, 3)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

if choice == 1:
    print(rock)
if choice == 2:
    print(paper)
if choice == 3:
    print(scissors)


if random_integer == 1:
    print("Computer chose:")
    print(rock)
if random_integer == 2:
    print("Computer chose:")
    print(paper)
if random_integer == 3:
    print("Computer chose:")
    print(scissors)

if choice == random_integer:
    print("It's a draw!")
elif choice == 1 and random_integer == 2:
    print("You lose!")
elif choice == 1 and random_integer == 3:
    print("You won!")
elif choice == 2 and random_integer == 1:
    print("You won!")
elif choice == 2 and random_integer == 3:
    print("You lose!")
elif choice == 3 and random_integer == 1:
    print("You lose!")
elif choice == 3 and random_integer == 2:
    print("You won!")
else:
    print("You NEED to type, 1, 2 or 3. Try again lol")