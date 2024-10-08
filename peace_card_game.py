# Import necessary modules
import random

# Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

# Create a deck of cards
deck = [(suit, rank) for suit in suits for rank in ranks]

# Shuffle the deck 
random.shuffle(deck)

# Split the deck into two hands
deck_middle = int(len(deck) / 2)
p1_cards = deck[:deck_middle]
p2_cards = deck[deck_middle:]


def card_comparison(p1_card, p2_card):

    p1_rank = ranks.index(p1_card[1])
    p2_rank = ranks.index(p2_card[1])

    if p1_rank > p2_rank:
        return 1
    elif p2_rank > p1_rank:
        return 2
    else:
        return 0  



def play_round(player1_hand, player2_hand):

    if len(player1_hand) == 0 or len(player2_hand) == 0:
        return   

    p1_card = player1_hand.pop(0)
    p2_card = player2_hand.pop(0)

    print(f"Player 1 plays {p1_card}, Player 2 plays {p2_card}")
    result = card_comparison(p1_card, p2_card)

    if result == 1:
        print("Player 1 wins the round")

    elif result == 2:
        print("Player 2 wins the round")

    else:
        print("War!")
        war(player1_hand, player2_hand) 



def war(player1_hand, player2_hand):
    """Handles the 'war' scenario when both cards are equal."""
    if len(player1_hand) < 5 or len(player2_hand) < 5:
        print("A player doesn't have enough cards for war!")
        return


    p1_wars = [player1_hand.pop(0) for _ in range(4)]
    p2_wars = [player2_hand.pop(0) for _ in range(4)]

    p1_card = p1_wars[-1]  
    p2_card = p2_wars[-1]

    print(f"Player 1 plays {p1_card}, Player 2 plays {p2_card}")
    result = card_comparison(p1_card, p2_card)

    if result == 1:
        print("Player 1 wins the war")

    elif result == 2:
        print("Player 2 wins the war")

    else:
        print("War continues!")
        war(player1_hand, player2_hand)  




def play_game():
    """Main function to run the game."""
    round_count = 0

    while round_count<26:
        round_count += 1
        print(f"\n--- Round {round_count} ---")
        play_round(p1_cards, p2_cards)
        if len(p1_cards) == 0:
            print("Player 2 wins the game!")
            break
        elif len(p2_cards) == 0:
            print("Player 1 wins the game!")
            break

# Call the main function to start the game
play_game()
