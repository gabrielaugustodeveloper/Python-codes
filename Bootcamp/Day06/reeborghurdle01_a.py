def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def loop_goal():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


number_of_hurdles = 6
while number_of_hurdles > 0:
    loop_goal()
    number_of_hurdles -= 1
    print(number_of_hurdles)