"""
This would be our main class structure for now
"""

class poker(object):
  
  def __init__(self):
    
		self.card_deck = []
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
		
	
    
  def five_of_kind(self):
    pass
  
  def straight_flush(self):
    pass
    
   def four_of_kind(self):
    pass
   
   def full_house(self):
    pass
   
   def flush(self):
    pass
    
   def straight(self):
    pass
    
   def three_of_kind(self):	
    pass
    
   def two_pair(self):
    pass
    
   def one pair(self):
    pass
   
   def high_card(self):
    pass
    
    ------------------------------------------
   def test_hand(self, player):
    """
    Test hand will run every possible hand, the regular 10 hands and the score 
    is the ranking of the hand, each function will return true or false
    """
    if player == 1:
		
		x = self.player1_cards
    elif player == 2:
		x = self.player2_cards
	
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
	
   
		
		
		
      
      
      
    
    
   
  
