import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""






# Unlimited deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards(player, pc):
    for card in range(2):
        player.append(random.choice(cards))
        pc.append(random.choice(cards))

def calculate_score(hand):
    score = sum(hand)

    # Ace adjustment (11 → 1)
    while score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)

    return score

# MAIN GAME LOOP
play_again = True

while play_again:
    user = []
    computer = []

    print(logo)

    deal_cards(user, computer)
    game_over = False

    while not game_over:
        user_score = calculate_score(user)
        computer_score = calculate_score(computer)

        print("\nYour cards:", user, "Score:", user_score)
        print("Computer's first card:", computer[0])

        if user_score > 21:
            print("\nYou went over 21. You lose :(")
            game_over = True

        elif user_score == 21:
            print("\nBlackjack! You win :)")
            game_over = True

        else:
            choice = input("Type 'y' to get another card, 'n' to pass: ").lower()

            if choice == "y":
                user.append(random.choice(cards))
                computer.append(random.choice(cards))
            else:
                print("\nYou chose to stand.")
                game_over = True

    #FINAL REVEAL
    user_score = calculate_score(user)
    computer_score = calculate_score(computer)

    print("\n=== FINAL RESULTS ===")
    print("Your final cards:", user, "Final score:", user_score)
    print("Computer final cards:", computer, "Final score:", computer_score)

    if user_score > 21:
        print("You lose!")
    elif computer_score > 21:
        print("You win!")
    elif user_score > computer_score:
        print("You win!")
    elif user_score < computer_score:
        print("You lose!")
    else:
        print("It's a draw!")

    # PLAY AGAIN?
    again = input("\nDo you want to play another match? (y/n): ").lower()
    if again != "y":
        play_again = False
        print("\nThanks for playing! ")
