import cards
my_deck = cards.Deck()
my_deck.shuffle()
a_card = my_deck.deal()

Community_cards = []
Player1_list = []
Player2_list = []

for i in range(2):
    Player1_list.append(my_deck.deal())
    Player2_list.append(my_deck.deal())

for i in range(5):
    Community_cards.append(my_deck.deal())

print("Community Cards: ",Community_cards)                     
print("\nPlayer 1:", Player1_list)
print("PLayer 2:", Player2_list)
print()

from itertools import combinations

player1_hand = []
player2_hand = []

comb = combinations(Community_cards, 3)
a = 1
for i in list(comb):
    print(a, "this is the combination", i)
    player1_hand = [] + Player1_list + list(i)
    print(a, player1_hand, "this is the players hand")
    print()
    a += 1

