def life_in_weeks(age):
    passed = age * 52
    left = 4680 - passed
    print(f"You have {left} weeks left.")

# Call your function with hard coded values
life_in_weeks(12)
