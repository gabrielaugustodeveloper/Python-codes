import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

# Unlimited deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards(player):
    for _ in range(2):
        player.append(random.choice(cards))

def calculate_score(hand):
    score = sum(hand)

    # Ace adjustment
    while score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)

    return score

def player_turn(player, name):
    game_over = False

    while not game_over:
        score = calculate_score(player)
        print(f"\n{name}'s cards: {player} | Score: {score}")

        if score > 21:
            print(f"{name} busted!")
            game_over = True
        elif score == 21:
            print(f"{name} has Blackjack!")
            game_over = True
        else:
            choice = input(f"{name}, type 'y' to hit or 'n' to stand: ").lower()
            if choice == "y":
                player.append(random.choice(cards))
            else:
                print(f"{name} stands.")
                game_over = True

#MAIN GAME LOOP

play_again = True

while play_again:
    player1 = []
    player2 = []

    print(logo)

    deal_cards(player1)
    deal_cards(player2)

    # Each player plays separately
    player_turn(player1, "Player 1")
    print("\n" * 30)  # hide cards from Player 2
    player_turn(player2, "Player 2")

    # Final scores
    score1 = calculate_score(player1)
    score2 = calculate_score(player2)

    print("\n=== FINAL RESULTS ===")
    print("Player 1 cards:", player1, "Score:", score1)
    print("Player 2 cards:", player2, "Score:", score2)

    if score1 > 21 and score2 > 21:
        print("Both players busted! It's a draw ")
    elif score1 > 21:
        print("Player 2 wins ")
    elif score2 > 21:
        print("Player 1 wins ")
    elif score1 > score2:
        print("Player 1 wins ")
    elif score2 > score1:
        print("Player 2 wins ")
    else:
        print("It's a draw ")

    # Play again?
    again = input("\nDo you want to play another match? (y/n): ").lower()
    if again != "y":
        play_again = False
        print("\nThanks for playing! ")
        #END OF THE GAME
