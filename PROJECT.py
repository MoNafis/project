"""
This would be our main class structure for now
"""
print("Let's play Poker!")
import random

class poker(object):
  
  def __init__(self):
    
		self.carddeck = [] 
		 # shuffled deck of cards
		self.shuffledeck = random.shuffle(self.carddeck)
		self.suits = ['H', 'S', 'D', 'C']
		self.ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
		
		self.player1_cards = []
		self.player2_cards = []
		self.community_cards = []
		
		
		self.player1_score = 0
		self.player2_score = 0
		
		self.player1_high = 0
		self.player2_high = 0
		
		
		"""
		we can use random to get 2 random cards for every player and
		5 random community cards and assign them here
		"""
		
  def card_deck(self):
	
	self.deletelist = []
	
	for i in self.community_cards:
		self.deletelist.append(i)
	
	self.deletelist.append(self.player1_cards[0])
	self.deletelist.append(self.player1_cards[1])
	self.deletelist.append(self.player2_cards[0])
	self.deletelist.append(self.player2_cards[1])
	
	for k in self.deletelist:
		self.shuffledeck.remove(k)
  

  def straight_flush(self, x):
    
			
	for i in self.suits:
			counter = 0
			
			for i in range(0, len(
			
    
   def four_of_kind(self, x):
	
	for i in ranks:

    		counter = 0
    		num1 = 0

    		if i == 'A':

        		num1 = 1

   		 elif i == 'J':
        		num1 =  11

    		elif i == 'Q':
        		num1 = 12
 
		elif i == 'K':
        		num1 = 13
			
		elif i == '1':
			num1 = 10

    		else:
        		num1 = 1
    
    		for  k in range ( 0 ,len(cards)):
    
			asd = cards[k][0]

			if asd == 'A':
			    num2 = 1

			elif asd == 'J':
			    num2 = 11

			elif asd == 'Q':
			    num2 = 12

			elif asd == 'K':
			    num2 = 13

			else:
			    	num2 = int(asd)


			if num2 == num1:
				

			    	counter+=1

			if counter == 4:
			    	return True
	  
    
   
   def full_house(self, x):
    pass
   
   def flush(self, x):
    pass
    
   def straight(self, player, cards):
 	if player == 1:
		x = player1_cards
	elif player == 2:	
		x = player2_cards
	num1 = len(x)	
    	for i in range ( num1):
			
		for k in range(0, num1 - 1):
				if x[k].get_value > x[k+1].get_value:
					x[k], x[k+1] = x[k+1], x[k]
	counter = 0
	for j in range(0, num1 - 1):
		if x[k].get_value - x[k+1].get_value == 1:
			counter+=1
		else:
			return False
	if counter == 5:
		return True		
   def three_of_kind(self, x):
	
	if x == 1:
		d = self.player1_cards
	elif x == 2:
		d = self.player2_cards
	
	for i in ranks:

    counter = 0
    num1 = 0

    if i == 'A':
        num1 = 1
	
    elif i == 'J':
        num1 =  11

    elif i == 'Q':
        num1 = 12

    elif i == 'K':
        num1 = 13
    
    elif i == '1':
	num1 = 10

    else:
        num1 = 1
    
    for  k in range ( 0 ,len(d)):
  
        asd = d[k][0]

        if asd == 'A':
            num2 = 1

        elif asd == 'J':
            num2 = 11
            
        elif asd == 'Q':
            num2 = 12

        elif asd == 'K':
            num2 = 13
	
	elif asd == '1':
	    num2 = 10

        else:
            num2 = int(asd)


        if num2 == num1:
            
            counter+=1
            
	if counter == 3:
	    return True
	  
    
    
   def two_pair(self, x):
	
	if x == 1:
		d = self.player1_cards
	elif x == 2:
		d = self.player2_cards
		
	
	
	for i in self.ranks:
			
			counter1 = 0
			
			for q in range(0,len(d)):
			
				c = d[q][0]
				
			if c == i:
				counter1+=1
			
			if counter1 == 2:
				break
			
			
				
	for i in self.ranks:
			
			counter2 = 0
			
			for q in range(0,len(d)):
			
				c = d[q][0]
				
			if c == i:
				counter2+=1
			
			if counter2 == 2:
				break
	
	if counter1 == 2 and counter2 == 2:
			return True
			
	else:
			return False
			
    
   def one pair(self, x):
			
    for i in self.ranks:
			
			counter = 0
			
			for q in range(0,len(d)):
			
				c = d[q][0]
				
			if c == i:
				counter+=1
			
			if counter == 2:
				break
     if counter == 2:
			return True
	 else:
			return False
			
			
   def high_card(self, x):
	
	if x == 1:
		d = self.player1_cards
	elif x == 2:
		d = self.player2_cards

	highest = 0
	
	for j in d:
		
		if j[0] == 'A':
			num1 = 1
		elif j[0] == 'J':
			num1 = 11
		elif j[[0] == 'Q':
		       num1 = 12
		elif j[0] == 'K':
		       num1 = 13
		
		elif j[0] == '1':
		       num1 = 10
		else:    
		       num1 = int(j[0])
		
		if num1 > highest:
			highest = num1
	return num1
    
    
    ------------------------------------------
   def test_hand(self, player):
    """
    Test hand will run every possible hand, the regular 10 hands and the score 
    is the ranking of the hand, each function will return true or false
    """
    if player == 1:
		
		r = self.player1_cards
		k = self.player1_score
		h = self.player1_high
    elif player == 2:
		r = self.player2_cards
		k = self.player2_score
		h = self.player2_high
	
    while 1 == 1:
        
	      
      if straight_flush(self, r) == True:
        k= 9
        break
        
      if four_of_kind(self, r) == True:
        k = 7
        break
        
      if full_house(self, r) == True:
        k = 6
        break
        
      if flush(self, r) == True:
        k = 5
        break
      
      if straight(self, r) == True:
        k = 4
        break
        
      if three_pair(self, r) == True:
        k = 3
        break
        
      if one_pair(self, r) == True:
        k = 2
        break
      

      self.score = 1
      h = high_card(self, x):
      break
		
  
    def player_compare(self):
	
	'''
    	compares the result of the 2 players and determines the winner
	'''
	
   
		
		
		
      
      
      
    
    
   
  
