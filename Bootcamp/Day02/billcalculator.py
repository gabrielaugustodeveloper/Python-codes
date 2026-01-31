print("Welcome to the tip calculator.py!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_str = str(tip)
totaltip = "1." + tip_str
#print(totaltip)


total = bill/people * float(totaltip)
print(f"The bill per person is ${total}")