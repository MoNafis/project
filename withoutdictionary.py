import cards
''' The basic process is this:
    1) You create a Deck instance, which is filled (automatically) with 52 Card instances
    2) You can deal those cards out of the deck into hands, each hand a list of cards
    3) You then manipulate cards as you add/remove them from a hand
'''

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

Player1_wins = []
Player2_wins = []

for i in Player1_list:
    Player1_wins.append(i)
for i in Community_cards:
    Player1_wins.append(i)

for i in Player2_wins:
    Player2_wins.append(i)
for i in Community_cards:
    Player2_wins.append(i)




print("Community Cards: ",Community_cards)                     
print("\nPlayer 1:", Player1_list)
print("PLayer 2:", Player2_list)

def isfour_of_kind(community,player):
    find_rank = []
    value_list= []
    
    find_rank.append(player[0])
    find_rank.append(player[1])
            
    for i in community:
         find_rank.append(i)

    for i in find_rank:
        Value = i.get_rank()
        value_list.append(Value)
        
    print(value_list)

    global straight1 
    for i in range(7):
        check = 0
        for j in range(7):
            if value_list[i] == value_list[j]:
                check += 1
                if check>=4:
                    return True
            else:
                pass


def isStraight(community,player):
    global straight1
    straight1 = []
    
    value_list = []
    
    alist = []
    
    straight1.append(player[0])
    straight1.append(player[1])
    for i in community:
        straight1.append(i)
    

    for i in straight1:
        Value = i.get_rank()
        value_list.append(Value)
        LL = value_list
        value_list.sort()
        

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

    if isfour_of_kind(community,player1) == True and isfour_of_kind(community,player2) == True:
        print("It is a tie with a four of a kind: ", Community_cards)
        
    elif isfour_of_kind(community,player1) == True:
        print("Player 1 wins with a four of a kind: ", Player1_wins)
        
    elif isfour_of_kind(community,player2) == True:
        print("Player 2 wins with a four of a kind: ", Player2_wins)
        
        
    if isStraight(community,player1) == True and isStraight(community,player2) == True:
        print("It is a tie with a straight: ",Community_cards)
        
    elif isStraight(community,player1) == True:
        print("Player 1 wins with a straight",straight1[0:5])
        
    elif isStraight(community,player2) == True:
        print("Player 2 wins with a straight",straight1[0:5])
        


main(Community_cards,Player1_list,Player2_list)
print(straight1)
