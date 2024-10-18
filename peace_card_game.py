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
    
    #Comparison 
    if p1_rank > p2_rank:
        return 1
    elif p2_rank > p1_rank:
        return 2
    else:
        return 0



def play_round(player1_hand, player2_hand):
    #Pick out the cards to be played
    p1_card = player1_hand.pop(0)
    p2_card = player2_hand.pop(0)
    print(f"Player 1 plays {p1_card}, Player 2 plays {p2_card}")
       
    # Compare the cards to determine the winner
    result = card_comparison(p1_card, p2_card)

    if result == 1:
        print("Player 1 wins the round")
        player1_hand.append(p1_card)
        player1_hand.append(p2_card)

    elif result == 2:
        print("Player 2 wins the round")
        player2_hand.append(p2_card)
        player2_hand.append(p1_card)

    #If tie, then start Peace!
    else:
        print("Peace!")
        player1_hand.append(p1_card)
        player2_hand.append(p2_card)
        war(player1_hand, player2_hand)



def war(player1_hand, player2_hand):
    player1_war_cards = []
    player2_war_cards = []

    #decide number of cards for peace, if less then 4, then do according to the deck with lesser
    war_deck_length = 4 if len(player1_hand)>4 and len(player2_hand)>4 else len(player1_hand) if len(player1_hand)<len(player2_hand) else len(player2_hand)


    # Pick top 4 cards pretty much
    for _ in range(war_deck_length):
        player1_war_cards.append(player1_hand.pop(0)) 
        player2_war_cards.append(player2_hand.pop(0))
    
    # Do the comparisons, card by card
    for n in range(war_deck_length):
        p1_card = player1_war_cards[n]
        p2_card = player2_war_cards[n]

        print(f"Player 1 plays {p1_card}, Player 2 plays {p2_card}")
        result = card_comparison(p1_card, p2_card)

        if result == 1:
            print("Player 1 wins the peace")
            player1_hand.extend(player1_war_cards + player2_war_cards)
            player1_hand.append(player2_hand.pop(-1)) if len(player2_hand)>=1 else player1_hand
            break

        if result == 2: 
            print("Player 2 wins the peace")
            player2_hand.extend(player1_war_cards + player2_war_cards)
            player2_hand.append(player1_hand.pop(-1)) if len(player1_hand)>=1 else player2_hand
            break
        
        #if we run out of cards without a victor
        if result == 0 and (len(player1_war_cards)<1 and len(player2_war_cards)<1):
            print("Restart peace")
            war(player1_hand, player2_hand)
            break

        #tie but we have cards left
        elif result == 0 and (len(player1_war_cards)>0 and len(player2_war_cards)>0):
            print("Peace continues!")



def play_game():
    round_count = 0

    while len(p1_cards) > 0 or len(p2_cards) > 0:
        round_count += 1
        print(f"\n--- Round {round_count} ---")
        play_round(p1_cards, p2_cards)

        # input("Press enter to continue: ")
        time.sleep(0.1)

        if len(p1_cards) == 0:
            print("Player 2 wins the game!")
            break

        elif len(p2_cards) == 0:
            print("Player 1 wins the game!")
            break

    #verify all went well:
    print(f"Player 1 cards: {len(p1_cards)}, Player 2 cards: {len(p2_cards)}")

#MAIN
play_game()

