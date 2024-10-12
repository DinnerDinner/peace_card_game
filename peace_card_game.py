import random
import time

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

    p1_card = player1_hand.pop(0)
    p2_card = player2_hand.pop(0)
    print(f"Player 1 plays {p1_card}, Player 2 plays {p2_card}")

    result = card_comparison(p1_card, p2_card)

    if result == 1:
        print("Player 1 wins the round")
        player1_hand.append(p1_card)
        player1_hand.append(p2_card)

    elif result == 2:
        print("Player 2 wins the round")
        player2_hand.append(p2_card)
        player2_hand.append(p1_card)

    else:
        print("War!")
        player1_hand.append(p1_card)
        player2_hand.append(p2_card)
        war(player1_hand, player2_hand)



def war(player1_hand, player2_hand):
    player1_war_cards = []
    player2_war_cards = []
    
    if len(player1_hand)<5 or len(player2_hand)<5: 
        print(" I have no clue, even the rulebook doesn't have anything about this :(, this assignement too hard, im gonna cry")
        print("I just make both players re-add the card to the bottom of their decks, avoiding loss of cards")

    else: 
        # Pick top 4 cards pretty much
        for _ in range(4):
            player1_war_cards.append(player1_hand.pop(0)) 
            player2_war_cards.append(player2_hand.pop(0))
        

        # Compare the cards to determine the winner
        for n in range(4):
            p1_card = player1_war_cards[n]
            p2_card = player2_war_cards[n]

            print(f"Player 1 plays {p1_card}, Player 2 plays {p2_card}")
            result = card_comparison(p1_card, p2_card)

            if result == 1:
                print("Player 1 wins the war")
                player1_hand.extend(player1_war_cards + player2_war_cards)
                player1_hand.append(player2_hand[-1])
                player2_hand.pop(-1)
                break

            if result == 2: 
                print("Player 1 wins the war")
                player2_hand.extend(player1_war_cards + player2_war_cards)
                player2_hand.append(player1_hand[-1])
                player1_hand.pop(-1)
                break

            if result == 0 and (len(player1_war_cards)<1 and len(player2_war_cards)<1):
                print("Restart war")
                war(player1_hand, player2_hand)
                break

            elif result == 0 and (len(player1_war_cards)>0 and len(player2_war_cards)>0):
                print("War continues!")



def play_game():
    round_count = 0

    while len(p1_cards) > 0 or len(p2_cards) > 0:
        round_count += 1
        print(f"\n--- Round {round_count} ---")
        play_round(p1_cards, p2_cards)

        # input("Press enter to continue: ")
        # time.sleep(0.1)

        if len(p1_cards) == 0:
            print("Player 2 wins the game!")
            break

        elif len(p2_cards) == 0:
            print("Player 1 wins the game!")
            break

    #verify all went well:
    print(f"Player 1 cards: {len(p1_cards)}, Player 2 cards: {len(p2_cards)}")


play_game()
