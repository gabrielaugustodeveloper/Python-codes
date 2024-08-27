height = 1.77
weight = 84
# Calculate the BMI using the formula: BMI = weight / (height^2)
# height^2 calculates the square of the height
# weight / (height^2) gives the BMI
bmi = weight / (height ** 2)

print(bmi)

print(int(bmi))

print(round(bmi))

print(round(bmi, 2))