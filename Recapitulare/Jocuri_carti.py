numbers = (2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A")
suits = "♤♡♧♢"

number_strength = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "J": 12, "Q": 13, "K": 14, "A": 15}

def make_deck(jokers=True):
    """
    This function should create a deck of ordered cards. It can add jokers or not do it, depending on jokers param.
    :param jokers: True or False if jokers should be added in this deck.
    :return: the created deck.
    """
    deck = [(number, suit) for number in numbers for suit in suits]

    if jokers:
        deck += [("Joker", "♤"), ("Joker", "♡")]

    return deck

def shuffle_deck(deck):
    """
    This function should return a shuffled deck.
    :param deck: the original unshuffled deck.
    :return: the new shuffled deck.
    """
    set_deck = set(deck)
    shuffled_deck = []
    for _ in range(len(deck)):
        shuffled_deck.append(set_deck.pop())

    return shuffled_deck

def deal_cards(deck, hands_nr=2, shuffle=False):
    """
    This function should deal the cards from a deck to a number of hands..
    :param deck: the original deck.
    :param hands_nr: the number of hands that the deck should be dealt to.
    :param shuffle: True or False if the deck should also be shuffled before.
    :return: a list of the hands with their dealt cards.
    """
    if shuffle:
        deck = shuffle_deck(deck)

    hands = [[] for _ in range(hands_nr)]
    for i, card in enumerate(deck):
        hands[i % hands_nr].append(card)

    return hands

def draw_card(deck):
    """
    This function should return a random card from the deck/hand. The card is removed from the deck/hand.
    :param deck: the original deck from which the card should be removed.
    :return: the random card from the deck/hand.
    """
    return deck.pop(0)

def get_card_strength(card):
    """
    This function should return the strength of a card.
    :param card: the card.
    :return: the strength of the card.
    """
    return number_strength[card[0]]

def war_manager():
    """
    This function should manage a war game between two players.
    """
    deck = make_deck(jokers=False)
    deck = shuffle_deck(deck)
    hand_1, hand_2 = deal_cards(deck)
    war_cards = []

    round_no = 1

    while len(hand_1) > 0 and len(hand_2) > 0:
        card_1 = draw_card(hand_1)
        card_2 = draw_card(hand_2)

        print(f"Round {round_no} -> {card_1} - {card_2}", end="")

        card_strength_1 = get_card_strength(card_1)
        card_strength_2 = get_card_strength(card_2)

        if card_strength_1 > card_strength_2:
            hand_1.extend(war_cards)
            hand_1.append(card_1)
            hand_1.append(card_2)
            war_cards.clear()
            print(" -> First player wins")
        elif card_strength_1 < card_strength_2:
            hand_1.extend(war_cards)
            hand_2.append(card_2)
            hand_2.append(card_1)
            war_cards.clear()
            print(" -> Second player wins")
        else:
            war_cards.append(card_1)
            war_cards.append(card_2)
            print(" -> It's a war!")

        round_no += 1

    if len(hand_1) > 0:
        print("First player wins this game!")
    else:
        print("Second player wins this game!")


if __name__ == "__main__":
    war_manager()
