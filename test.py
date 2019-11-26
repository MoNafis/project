"""docstring."""

suit_list = ['x', 'c', 'd', 'h', 's']
rank_list = ['x', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q'
             '\n', 'K']
'''

list1 = ['8C', '9C', '2D', '7C', '3S']  # in this case use k as 12
high = 0
for i in list1:

    print(i, i[0])

    if int(i[0]) > high:
        high  = int(i[0])
        print(high)
'''
# Yay guthub pushes are working
ranklist = ['A', 'J', 'Q', 'K']

list2 = ['10S', '8H', '2D']
high = 0
for i in list2:
    # print(i[0], i[1], "AND ME",i[0][0],"mME ")#how is i[0]the same as i[0][0]

    print(i[0], "HERE", i)

    if len(i) > 2:

        if int(i[0] + i[1]) > high:

            high = int(i[0] + i[1])
            print(high)

    elif len(i) == 2:

        if int(i[0]) > high:

            high = int(i[0])
            print(high, "this is the final high")
    else:
        print("invalid card , as it cannot have a length of less than 2")

    '''
    if i[0] > high:
        high = int(i[0])
print(high)
'''
# for j in i
# print(j)




'''
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
Community_cards=['9h','8c','7d','10h','8s'] 
Player1_list=['5h','6s']
Player2_list=['7a', 'Qd']

def isStraight(community,player):
    straight = []
    
    value_list = []
    
    alist = []
    
    straight.append(str(player[0]))
    straight.append(str(player[1]))
    for i in Community_cards:
        straight.append(str(i))
    print(straight)

    
    for i in straight:
        find_value = my_dict.get(str(i))
        print(i)
        value_list.append(find_value)
        LL = value_list
        
        value_list.sort()
    
    alist = list(set(value_list))
    

    if len(alist)>4:

        if  (alist[4] - alist[0]) == 4:
            for i in alist:
                if LL[0] == i or LL[0] == i:
                    return True
        else:
                return False

def main(community,player1,player2):
    if isStraight(community,player1) == True and isStraight(community,player2) == True:
        print("It is a tie with straight")
    elif isStraight(community,player1) == True:
        print("Player 1 wins")
    elif isStraight(community,player2) == True:
        print("Player 2 wins")



main(Community_cards,Player1_list,Player2_list)

'''
