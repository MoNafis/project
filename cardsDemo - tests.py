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
    

def isStraight(community,player):
    straight1 = []
    
    value_list = []
    
    alist = []
    
    straight1.append(str(player[0]))
    straight1.append(str(player[1]))
    for i in community:
        straight1.append(str(i))
    

    
    for i in straight1:
        find_value = my_dict.get(i)
        value_list.append(find_value)
        LL = value_list
        value_list.sort()
    print(value_list)
    alist = list(set(value_list))

    if len(alist)>4:

        if  (alist[4] - alist[0]) == 4:
            for i in alist:
                if LL[0] == i or LL[0] == i:
                    return True
                    break
        else:
                return False

def main(community,player1,player2):
    if isStraight(community,player1) == True and isStraight(community,player2) == True:
        print("It is a tie with: ","need to return communitycards here")
    elif isStraight(community,player1) == True:
        print("Player 1 wins","need to return winning hand for player1 here")
    elif isStraight(community,player2) == True:
        print("Player 2 wins","need to return winning hand player2 here")


main(Community_cards,Player1_list,Player2_list)
