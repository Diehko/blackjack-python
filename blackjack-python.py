import random 
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':[1,11]}

class Cards:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.allcards = []

    def build_deck(self):
        for suit in suits:
            for rank in ranks:
                self.allcards.append(Cards(suit,rank))
                
    def shuffle_cards(self):
        random.shuffle(self.allcards)

class Deal_Cards:
    def __init__(self):
        self.playerturn = 1
        self.dealerturn = 1
        
    def deal_player_cards(self, deck):
        PlayerCards = ''
        PlayerCards = deck.pop()
        return PlayerCards 

    def deal_dealer_cards(self, deck):
        DealerCards = ''
        DealerCards = deck.pop()
        return DealerCards

class Card_Conversion_Sum():
    def __init__(self):
        self.PlayerPlay = []
        self.DealerPlay = []
        self.PlayerAceList = []
        self.DealerAceList = []

    def reset_player_lists(self):
        self.PlayerPlay = []
        self.PlayerAceList = []

    def reset_dealer_lists(self):
        self.DealerPlay = []
        self.DealerAceList = []
        
    def convert_to_int_player(self, playercard):
        rank = str(playercard).split()[0]
        if rank == 'Ace':
            self.PlayerAceList.append(rank)
        else:
            self.PlayerPlay.append(values[rank])

                
    def convert_to_int_dealer(self, dealerdeckvalues):
        rank = str(dealerdeckvalues).split()[0]
        if rank == 'Ace':
            self.DealerAceList.append(rank)
        else:
            self.DealerPlay.append(values[rank])
                
    def sum_player_values(self):
        self.Playersum = 0
        i = 0
        while i < len(self.PlayerPlay):
            self.Playersum = self.Playersum + self.PlayerPlay[i]
            i+=1

        if len(self.PlayerAceList) != 0:
            n=0
            while n < len(self.PlayerAceList):
                if self.Playersum > 10 and self.Playersum < 21:
                    self.Playersum+=1
                elif self.Playersum <= 10:
                    self.Playersum+=11
                else:
                    self.Playersum+=1
                    break
                n+=1
        return self.Playersum


            
    def sum_dealer_values(self):
        self.Dealersum = 0
        i = 0
        while i < len(self.DealerPlay):
            self.Dealersum = self.Dealersum + self.DealerPlay[i]
            i+=1

        if len(self.DealerAceList) != 0:
            n=0
            while n < len(self.PlayerAceList):
                if self.Dealersum > 6 and self.Playersum < 17:
                    self.Dealersum+=1
                elif self.Dealersum <= 6:
                    self.Dealersum+=11
                else:
                    self.Dealersum+=1
                    break
        return self.Dealersum

        
    


begingame = Deck()  #Begingame created as instance of Deck class
begingame.build_deck() #The main Deck is created
begingame.shuffle_cards() #The main Deck is shuffled
dealcards = Deal_Cards() #dealcards created as instance of Deal_Cards class
sum_conversion = Card_Conversion_Sum() #sum_conversion created as instance of Card_Conversion_Sum class
b_dealer = 0   #b_dealer variable created to store dealer value sum
nplayers = 1
Game_on = True #Variable to create
dealerdeck = []
number_of_players = int(input("How many players are going to play?: ")) #Number of players stored in the variable number_of_players
players_dict = {} #Dictionary created to store player's deck, player's deck sum, and initial player question
Done_list = [] #List created to append player's deck sum
Dealer_BlackJack = False
Player_BlackJack = False
while nplayers <= number_of_players: #Create Pn dictionary, with the number of keys equal to the nunmber of players, to store player's deck, player's deck sum, and initial player question, per player. 
    a = 'P' + str(nplayers) #The Pn dictionary key is created for each player
    players_dict[a] = {'DECK':[],'SUM':0,'PLAYER_QUESTION':'HIT'} #Players initiate with an empty deck, a sum of 0, and question 'HIT'
    nplayers+=1

##########################################################################################
######################################DEALING CARDS#######################################
##########################################################################################
turn = 1
dealerdeckvalues = 0
while dealerdeckvalues < 2:
    dealerdeck.append(dealcards.deal_dealer_cards(begingame.allcards))
    sum_conversion.convert_to_int_dealer(dealerdeck[dealerdeckvalues])
    dealerdeckvalues+=1
b_dealer = sum_conversion.sum_dealer_values()

nplayers = 1
while nplayers <= number_of_players:
    a = 'P' + str(nplayers)
    deckvalues = 0
    while deckvalues < 2:
        players_dict[a]['DECK'].append(dealcards.deal_player_cards(begingame.allcards))
        sum_conversion.convert_to_int_player(players_dict[a]['DECK'][deckvalues])
        deckvalues+=1      
    players_dict[a]['SUM'] = sum_conversion.sum_player_values()
    print("---------------------------------")
    print(f"First two Player's {nplayers} deck: ")
    print("---------------------------------")
    for f in players_dict[a]['DECK']:
        print(f)
    sum_conversion.reset_player_lists()
    nplayers+=1

print("#################################")
print("First Dealer card: ")
print("#################################")
print(dealerdeck[0])

##########################################################################################
######################################SECOND TURN#######################################
##########################################################################################

#######################################
#CHECKING IF THE DEALER HAS BLACK JACK#
#######################################
if b_dealer == 21 and turn == 1:
    print("The DEALER has BLACKJACK")
    Dealer_BlackJack = True

###########################
#CHECKING ALL THE PLAYERS#
###########################
nplayers = 1
while nplayers <= number_of_players:
    a = 'P' + str(nplayers)
    turn = 1
    ########################
    #GRAB CARTS PER PLAYERS#
    ########################
    while True:
        if players_dict[a]['SUM'] == 21 and turn == 1:
            print(f"Player {nplayers} has BLACKJACK")
            sum_conversion.reset_player_lists()
            break
        elif players_dict[a]['SUM'] == 21:
            print(f" Player {nplayers} has 21")
            sum_conversion.reset_player_lists()
            break
        elif players_dict[a]['SUM'] > 21:
            print(f"The Player {nplayers} BUST")
            sum_conversion.reset_player_lists()
            break
        while True:
            Question = input(f"Player {nplayers}, Do you want to STAY or HIT: ")
            if Question.upper() not in ['STAY','HIT']:
                print("Please type 'STAY' or 'HIT'")
            else:
                break
        if Question.upper() == 'HIT':    
            players_dict[a]['DECK'].append(dealcards.deal_player_cards(begingame.allcards))
            deckvalues = 0
            players_dict[a]['SUM'] = 0
            sum_conversion.reset_player_lists()
            while deckvalues < len(players_dict[a]['DECK']):
                sum_conversion.convert_to_int_player(players_dict[a]['DECK'][deckvalues])  
                players_dict[a]['SUM'] = sum_conversion.sum_player_values()
                deckvalues+=1
            turn = 2
            print("---------------------------------")
            print(f"Player's {nplayers} deck:")
            print("---------------------------------")
            for i in players_dict[a]['DECK']:
                print(i)
            print(f"The value so far is:{players_dict[a]['SUM']}")
        elif Question.upper() == 'STAY':
            print(f"Player {nplayers} stayed in {players_dict[a]['SUM']}")
            sum_conversion.reset_player_lists()
            break

    nplayers+=1

####################
#GRAB CARTS DEALER#
###################
print("#################################")
print("Dealer Deck: ")
print("#################################")
for i in dealerdeck:
    print(i)
        
while Dealer_BlackJack == False:
    if b_dealer < 17:
        sum_conversion.reset_dealer_lists()
        dealerdeck.append(dealcards.deal_dealer_cards(begingame.allcards))
        dealerdeckvalues = 0
        while dealerdeckvalues < len(dealerdeck):
            sum_conversion.convert_to_int_dealer(dealerdeck[dealerdeckvalues])
            b_dealer = sum_conversion.sum_dealer_values()
            dealerdeckvalues+=1
        print("#################################")
        print("Dealer deck: ")
        print("#################################")
        for i in dealerdeck:
            print(i)
        print(f"The value so far is:{b_dealer}")
    elif b_dealer >= 17 and b_dealer < 21:
        print(f"The dealer statyed with {b_dealer}")
        break
    elif b_dealer == 21:
        print("The dealer has 21")
        break
    elif b_dealer > 21:
        print ("The dealer BUST")
        break
 

