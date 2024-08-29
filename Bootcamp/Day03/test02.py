print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age <= 55 and age >= 45:
        bill = 0
        print("Midlife don't pay :D!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    photo = input("Do you want a photo?(Type y for yes and n for no)")
    if photo == "y":
        bill = bill + 3 #Or bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
