def is_leap_year(year):

    leap = False

    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True

    return leap


print(is_leap_year(2026))