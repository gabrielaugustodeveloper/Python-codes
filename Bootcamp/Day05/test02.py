student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

print(max(student_scores))

total = sum(student_scores)
print(total)

max = 0
for number in student_scores:
    if max > number:
        max = max
    elif max < number:
        max = number
print(max)

sum = 0
for score in student_scores:
    sum += score
print(sum)


