def turn_right():

    turn_left()

    turn_left()

    turn_left()

#Solution for Hurdles with Variable Heights

while not at_goal():

    if front_is_clear():

        move()

        if right_is_clear():

            turn_right()

    elif wall_in_front():

        turn_left()