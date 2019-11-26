import cards
''' The basic process is this:
    1) You create a Deck instance, which is filled (automatically) with 52 Card instances
    2) You can deal those cards out of the deck into hands, each hand a list of cards
    3) You then manipulate cards as you add/remove them from a hand
'''
value = 0
my_dict = {}
my_deck = cards.Deck()

LocalDeck = str(my_deck)
LocalDeck = LocalDeck.split(',')

for i in LocalDeck:
    my_dict[i] = value
    value = (value+1)%13
print(my_dict)
    

my_deck = cards.Deck()
my_deck.shuffle()


a_card = my_deck.deal()



print("Dealt card is:",a_card)
print('How many cards left:',my_deck.cards_count())

print("Is the deck empty?",my_deck.is_empty())

# deal some hands and print
Community_cards=[] 
Player1_list=[]
Player2_list=[]
for i in range(2):
    Player1_list.append(my_deck.deal())
    Player2_list.append(my_deck.deal())

for i in range(5):
    Community_cards.append(my_deck.deal())

a = []
a.append(Player1_list)
a.append(Player2_list)
a.append(Community_cards)
print(a)
print("Community Cards: ",Community_cards)                     
print("\nPlayer 1:", Player1_list)
print("PLayer 2:", Player2_list)
    

def isStraight():
    straight1 = []
    
    value_list = []
    
    alist = []
    
    straight1.append(str(Player1_list[0]))
    straight1.append(str(Player1_list[1]))
    for i in Community_cards:
        straight1.append(str(i))
    print(straight1)

    
    for i in straight1:
        find_value = my_dict.get(i)
        value_list.append(find_value)
        LL = value_list
        value_list.sort()
        
    alist = list(set(value_list))



    if  (alist[4] - alist[0]) == 4:
        for i in alist:
            if LL[0] == i or LL[0] == i:
                print('Player 1 wins with a Straight: ',straight1[0:5])
                break
    else:
            print('not a straight')
isStraight()
