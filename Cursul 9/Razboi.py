numbers = ("A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K")
suits = "♤♡♧♢"

nunber_strength = {"A": 15, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "J": 12, "Q": 13, "K": 14}

all_cards = {(number, suit) for number in numbers for suit in suits}

first_hand = []
second_hand = []

while all_cards:
    first_hand.append(all_cards.pop())
    second_hand.append(all_cards.pop())

first_card = first_hand.pop()
second_card = second_hand.pop()
print(first_card, second_card)
if nunber_strength[first_card[0]] > nunber_strength[second_card[0]]:
    print("Primul are o carte mai mare")
elif nunber_strength[first_card[0]] < nunber_strength[second_card[0]]:
    print("Al doilea are o carte mai mare")
else:
    print("Cartile sunt egale")

# numbers = {f"{num}" for num in range(1, 50)}
# print(numbers.pop())
# print(numbers.pop())
# print(numbers.pop())
# print(numbers.pop())
# print(numbers.pop())
