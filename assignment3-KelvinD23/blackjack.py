import random
BLACKJACK = 21
FACE_CARD_VALUE = 10
ACE_VALUE = 1
CARD_LABELS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
BLACKJACK = 21
DEALER_THRESHOLD = 16

def deal_card():
    """Evaluates to a character representing one of 13
    cards in the CARD_LABELS tuple

    :return: a single- or double-character string representing a playing card

    >>> random.seed(13)
    >>> deal_card()
    '5'
    >>> deal_card()
    '5'
    >>> deal_card()
    'J'
    """

    return random.choice(CARD_LABELS)

def get_card_value(card_label):
    """Evaluates to the integer value associated with
    the card label (a single- or double-character string)

    :param card_label: a single- or double-character string representing a card
    :return: an int representing the card's value

    >>> card_label = 'A'
    >>> get_card_value(card_label)
    1
    >>> card_label = 'K'
    >>> get_card_value(card_label)
    10
    >>> card_label = '5'
    >>> get_card_value(card_label)
    5
    """
    if card_label != "K" and card_label != "A" and card_label != "Q" and card_label != "J":
        return int(card_label)

    if card_label == "K" or card_label == "Q" or card_label == "J":
        return FACE_CARD_VALUE
    if card_label == "A":
        return ACE_VALUE

def deal_cards_to_player():
    """Deals cards to the player and returns the card
    total

    :return: the total value of the cards dealt
    """

    card1 = deal_card()
    card2 = deal_card()
    pc1_value = get_card_value(card1)
    pc2_value = get_card_value(card2)
    player_total = (pc1_value + pc2_value)

    print("Player drew " + str(card1) + " and " + str(card2) + ".")
    print("Player's total is {}.".format(player_total))
    print()


    while  player_total <= BLACKJACK:
        check = False
        while not check: #not check == True, check == False.. not False == True
            request_card = input("Hit (h) or Stay (s)? ") #ask for input
            print()
            check = request_card == "h" or request_card == "s"
        if (request_card == "h"):
            extra_card = deal_card()
            extra_card_value = get_card_value(extra_card)
            player_total = player_total + extra_card_value
            print("Player drew {}.".format(extra_card))
            print("Player's total is {}.".format(player_total))
            print()
        if ((request_card == "s")):
            break

    return player_total

def deal_cards_to_dealer():
    """Deals cards to the dealer and returns the card
    total

    :return: the total value of the cards dealt
    """
    dealer_card1 = deal_card()
    dc1_value = get_card_value(dealer_card1)
    dealer_card2 = deal_card()
    dc2_value = get_card_value(dealer_card2)
    dealer_total = (dc1_value + dc2_value)

    print("The dealer has " + str(dealer_card1) + " and " + str(dealer_card2) + ".")
    print("Dealer's total is {}.".format(dealer_total))
    print()

    while dealer_total <= DEALER_THRESHOLD:
        extra_card = deal_card()
        extra_card_value = get_card_value(extra_card)
        dealer_total = dealer_total + extra_card_value
        print("Dealer drew {}.".format(extra_card))
        print("Dealer's total is {}.".format(dealer_total))
        print()



    return dealer_total



def determine_outcome(player_total, dealer_total):
    """Determines the outcome of the game based on the value of
    the cards received by the player and dealer. Outputs a
    message indicating whether the player wins or loses.

    :param player_total: total value of cards drawn by player
    :param dealer_total: total value of cards drawn by dealer
    :return: None
    """

    if (player_total > BLACKJACK):
        print("YOU LOSE!")


    elif (player_total > dealer_total):
        print("YOU WIN!")


    elif dealer_total > BLACKJACK:
        print("YOU WIN!")


    else:
        print("YOU LOSE!")

    print()





def play_blackjack():
    """Allows user to play Blackjack by making function calls for
    dealing cards to the player and the dealer as well as
    determining a game's outcome

    :return: None
    """
    print("Let's Play Blackjack!")
    print()

    #loop to continue until game ends
    dealer = 0
    while True:
        # init player  = dealcards to player
        player = deal_cards_to_player()


        if player < BLACKJACK:
            dealer = deal_cards_to_dealer()
        determine_outcome(player, dealer)

        check = False
        while not check: #not check == True, check == False.. not False == True
            request = input("Play again (Y/N)?") #ask for input
            print()
            check = request == "Y" or request == "N"

        if request == "N":
            break

    print("Goodbye.")
####### DO NOT EDIT ABOVE ########

def main():
    """Runs a program for playing Blackjack with one player
    and a dealer
    """

    # call play_blackjack() here and remove pass below
    play_blackjack()



####### DO NOT REMOVE IF STATEMENT BELOW ########

if __name__ == "__main__":
    #Remove comments for next 4 lines to run doctests
    #print("Running doctests...")
    #import doctest
    #doctest.testmod(verbose=True)

    #print("\nRunning program...\n")

    main()
