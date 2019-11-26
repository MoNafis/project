"""
This would be our main class structure for now
"""

import random

class poker(object):
  
  def __init__(self):
    
		self.carddeck = [] 
		 # shuffled deck of cards
		self.shuffledeck = random.shuffle(self.carddeck)
		
		self.suits = ['H', 'S', 'D', 'C']
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
    
  def five_of_kind(self, x):
    pass
  
  def straight_flush(self, x):
    pass
    
   def four_of_kind(self, x):
	
	if x == 1:
		d = self.player1_cards
	elif x == 2:
		d = self.player2_cards
	
	for s in self.suits:
		
		counter = 0
		
		for r in range( len(d)):
			
			if [0] == s:
				counter+=1
			if counter == 4:
				return True
				break
    
   
   def full_house(self, x):
    pass
   
   def flush(self, x):
    pass
    
   def straight(self, x):
    pass
    
   def three_of_kind(self, x):
	
	if x == 1:
		d = self.player1_cards
	elif x == 2:
		d = self.player2_cards
	
	for s in self.suits:
		
		counter = 0
		
		for r in range( len(d)):
			
			if r[0] == s:
				counter+=1
			if counter == 3:
				return True
				break
    
    
   def two_pair(self, x):
    pass
    
   def one pair(self, x):
    pass
   
   def high_card(self, x):
    pass
    
    ------------------------------------------
   def test_hand(self, player):
    """
    Test hand will run every possible hand, the regular 10 hands and the score 
    is the ranking of the hand, each function will return true or false
    """
    if player == 1:
		
		r = self.player1_cards
    elif player == 2:
		r = self.player2_cards
	
    while 1 == 1:
      
      test_hand(self, x)
      
      if test_hand(self, x) == True:
        self.score = 9
        break
        
      if straight_flush(self, x) == True:
        self.score = 8
        break
        
      if four_of_kind(self, x) == True:
        self.score = 7
        break
        
      if full_house(self, x) == True:
        self.score = 6
        break
        
      if flush(self, x) == True:
        self.score = 5
        break
      
      if straight(self, x) == True:
        self.score = 4
        break
        
      if three_pair(self, x) == True:
        self.score = 3
        break
        
      if one_pair(self, x) == True:
        self.score = 2
        break
      

      self.score = 1
      self.high_number = high_card(self, x):
      break
		
  
    def player_compare(self):
	
	'''
    	compares the result of the 2 players and determines the winner
	'''
	
   
		
		
		
      
      
      
    
    
   
  
