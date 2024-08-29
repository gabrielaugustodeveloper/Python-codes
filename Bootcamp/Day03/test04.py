print("Welcome to Python Pizza Deliveries!")
bill = 0
size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    bill = bill + 15
if size == "M":
    bill = bill + 20
if size == "L":
    bill = bill + 25
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        bill = bill + 2
    else:
        bill = bill + 3
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill = bill + 1
print(f"Your final bill is: ${bill}.")

