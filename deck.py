import random

"""Three constants used for computing later on"""
CARDS = []
SUITS = ["Spades", "Clubs", "Diamonds", "Hearts"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

"""Populates the deck based on existing suits and ranks"""
for suit in SUITS:
    for rank in RANKS:
        CARDS.append(f"{rank} of {suit}")


def check_cards(card1, card2):
    """Checks which card is higher. In case of same rank checks for higher suit"""
    _card1 = card1.split()
    _card2 = card2.split()
    index1, index2 = RANKS.index(_card1[0]), RANKS.index(_card2[0])
    if not index1 == index2:
        return card1 if index1 > index2 else card2
    else:
        return card1 if SUITS.index(_card1[2]) > SUITS.index(_card1[2]) else card2


def pick_cards(num):
    """Picks num cards into each hand, makes sure there are no repetitions by removing specific card from the deck"""
    first_hand = []
    second_hand = []
    deck = CARDS[:]
    for i in range(num):
        card = random.choice(deck)
        first_hand.append(card)
        deck.remove(card)
    for i in range(num):
        card = random.choice(deck)
        second_hand.append(card)
        deck.remove(card)
    return first_hand, second_hand


def compare_hands(first_hand, second_hand):
    """Compares both hands for a length of smaller hand, prints higher cards and presents total number of wins"""
    no_of_comparisions = min(len(first_hand), len(second_hand))
    result = []
    for i in range(no_of_comparisions):
        result.append(check_cards(first_hand[i], second_hand[i]))
        print(result[i])
    total_first_hand = 0
    for card in first_hand:
        if card in result:
            total_first_hand += 1
    return f"The result has been presented above for first {no_of_comparisions} cards. First hand had {total_first_hand} winning cards, while second hand had {len(result) - total_first_hand} of them."


def present_hands(first_hand, second_hand):
    return f"First hand: {', '.join(first_hand)} \nSecond hand: {', '.join(second_hand)}"


first_hand, second_hand = pick_cards(5)
print(present_hands(first_hand, second_hand))
print(compare_hands(first_hand, second_hand))
