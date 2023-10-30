from random import shuffle
from abc import ABC, abstractmethod

HOUSE_HAND_INDEX = 0

#create a shoe (global variable) of 6 decks which is shuffled randomly
def create_shoe():
    global shoe
    #this is an array that contains 6 of each type of card from a standard 52 
    #card deck
    cards = ["AH", "AH", "AH", "AH", "AH", "AH", "AD", "AD", "AD", "AD", "AD", "AD", "AC", "AC", "AC", "AC", "AC", "AC", "AS", "AS", "AS", "AS", "AS", "AS", "KH", "KH", "KH", "KH", "KH", "KH", "KD", "KD", "KD", "KD", "KD", "KD", "KC", "KC", "KC", "KC", "KC", "KC", "KS", "KS", "KS", "KS", "KS", "KS", "QH", "QH", "QH", "QH", "QH", "QH", "QD", "QD", "QD", "QD", "QD", "QD", "QC", "QC", "QC", "QC", "QC", "QC", "QS", "QS", "QS", "QS", "QS", "QS", "JH", "JH", "JH", "JH", "JH", "JH", "JD", "JD", "JD", "JD", "JD", "JD", "JC", "JC", "JC", "JC", "JC", "JC", "JS", "JS", "JS", "JS", "JS", "JS", "10H", "10H", "10H", "10H", "10H", "10H", "10D", "10D", "10D", "10D", "10D", "10D", "10C", "10C", "10C", "10C", "10C", "10C", "10S", "10S", "10S", "10S", "10S", "10S", "9H", "9H", "9H", "9H", "9H", "9H", "9D", "9D", "9D", "9D", "9D", "9D", "9C", "9C", "9C", "9C", "9C", "9C", "9S", "9S", "9S", "9S", "9S", "9S", "8H", "8H", "8H", "8H", "8H", "8H", "8D", "8D", "8D", "8D", "8D", "8D", "8C", "8C", "8C", "8C", "8C", "8C", "8S", "8S", "8S", "8S", "8S", "8S", "7H", "7H", "7H", "7H", "7H", "7H", "7D", "7D", "7D", "7D", "7D", "7D", "7C", "7C", "7C", "7C", "7C", "7C", "7S", "7S", "7S", "7S", "7S", "7S", "6H", "6H", "6H", "6H", "6H", "6H", "6D", "6D", "6D", "6D", "6D", "6D", "6C", "6C", "6C", "6C", "6C", "6C", "6S", "6S", "6S", "6S", "6S", "6S", "5H", "5H", "5H", "5H", "5H", "5H", "5D", "5D", "5D", "5D", "5D", "5D", "5C", "5C", "5C", "5C", "5C", "5C", "5S", "5S", "5S", "5S", "5S", "5S", "4H", "4H", "4H", "4H", "4H", "4H", "4D", "4D", "4D", "4D", "4D", "4D", "4C", "4C", "4C", "4C", "4C", "4C", "4S", "4S", "4S", "4S", "4S", "4S", "3H", "3H", "3H", "3H", "3H", "3H", "3D", "3D", "3D", "3D", "3D", "3D", "3C", "3C", "3C", "3C", "3C", "3C", "3S", "3S", "3S", "3S", "3S", "3S", "2H", "2H", "2H", "2H", "2H", "2H", "2D", "2D", "2D", "2D", "2D", "2D", "2C", "2C", "2C", "2C", "2C", "2C", "2S", "2S", "2S", "2S", "2S", "2S"]
    shuffle(cards)
    shoe = cards
        
        
#remove and return the first element from the shoe
def pop_shoe():
    card = shoe[0]
    shoe.remove(card)
    
    #reshuffle the shoe if the shoe has run out
    if len(shoe) == 0:
        print("The shoe has run out and a new shoe is being shuffled.")
        create_shoe()
    return card


#create the parent class for the house and guests
class Player(ABC):
    def __init__(self, name):
        #set up 4 hands for each player, as each player can potentially split
        #up to 3 times to give a max of 4 hands
        self.name = name #player name
        self.value = [0, 0, 0, 0] #value of each hand
        self.result = [0, 0, 0, 0] #result of each hand (bust or stand)
    
    #return player name
    def get_name(self): 
        return self.name
    
    #return the current hand
    def get_hand(self, hand_index): 
        return self.hand[hand_index]
    
    #add the newest card to the players hand
    def set_hand(self, card, hand_index):
        self.hand[hand_index].append(card)
        
    #reset the hand and other variables (at the start of each hand)
    def reset_hand(self):
        self.hand = [[], [], [], []]
        self.hand_index = 0
        self.has_split = 0
        
    #get the index for the current hand    
    def get_hand_index(self):
        return self.hand_index
    
    #set the index for the current hand
    def set_hand_index(self, hand_index):
        self.hand_index = hand_index
    
    #add up the total value of the player's hand
    def get_value(self, hand):
        ace = 0 #track whether or not there is an ace, who's value can change
        value = 0
        
        #add up the total value of cards
        for card in hand:
            if card[0] == "A":
                ace += 1
                value += 11
            elif card[0] == "K" or card[0] == "Q" or card[0] == "J" or card[0] == "1":
                value += 10
            else:
                value += int(card[0])
        
        #if the hand value is over 21 and theres an ace change the value of the ace
        if value > 21:
            while ace > 0 and value > 21:
                ace -= 1
                value -= 10
        return value
    
    
    #set hand value
    def set_value(self, value, hand_index):
        self.value[hand_index] = value
    
    #get hand result
    def get_result(self, hand_index):
        return self.result[hand_index]
    
    #set hand result
    def set_result(self, result, hand_index):
        self.result[hand_index] = result
        
    #print the player's hand in a readable fashion
    def print_hand(self, hand):
        print(self.name, "hand:", end = " ")
        for card in hand:
            print(card, end = " ")
        print()
    
    #have the player take their turn, different for guests and the house
    @abstractmethod
    def action(self):
        pass    


#create the house class
class House(Player):
    def __init__(self,name):
        super().__init__(name)
        
    #take the house's turn, set result to 2 on bust, and result to 1 on stand 
    #set value to the hand value   
    def action(self):
        hand_index = 0
        while True:
            value = self.get_value(self.get_hand(HOUSE_HAND_INDEX))
            if value > 21:
                self.print_hand(self.get_hand(HOUSE_HAND_INDEX))
                self.set_result(2, HOUSE_HAND_INDEX)
                self.set_value(value, HOUSE_HAND_INDEX)
                print("dealer busts!")
                return
            elif value >= 17:
                self.print_hand(self.get_hand(HOUSE_HAND_INDEX))
                self.set_result(2, HOUSE_HAND_INDEX)
                self.set_value(value, HOUSE_HAND_INDEX)
                print("dealer stands at", str(value) + ".")
                return
            self.set_hand(pop_shoe(), HOUSE_HAND_INDEX)                             
            
    
    #print the house's hand in a readable fashion, this version hides the 
    #first card
    def print_hand_hidden(self):
        print(self.name, "hand:", end = " ")
        for card in range(len(self.hand[HOUSE_HAND_INDEX])):
            if card == 0:
                print("?", end = " ") #hide the first card
            else:
                print(self.hand[HOUSE_HAND_INDEX][card], end = " ")
        print()


#create the guest class, for each real player
class Guest(Player):
    def __init__(self,name):
        super().__init__(name)
        self.money = 1500
        self.bet_size = 0
        self.has_split = 0
        self.hand = [[], [], [], []]
        self.hand_index = 0 #index for keeping track of split hands
        self.value = [0, 0, 0, 0] #value of each hand
        self.result = [0, 0, 0, 0] #result of each hand (bust or stand)
    
    #get the user input for the action they want to take, if the action is 
    #not exactly a valid command then keep asking for user input
    #set result to 2 if they bust or 1 if they have stood
    #set value to the hand value
    def action(self):
        num_splits = 0 #keep track of how many hands were split
        while(True):
            #get the cards for the current hand
            hand_index = self.get_hand_index()
            hand = self.get_hand(hand_index)
            self.print_hand(hand)
            
            #act on the current hand
            action = input("Please take an action (hit, split, double down or stand): ")
            if action == "hit":
                self.set_hand(pop_shoe(), hand_index) #add the next card to the players hand
                value = self.get_value(hand)
                self.set_value(value, hand_index)
                if value > 21: #if player busts
                    #print player hand
                    print("bust!")
                    self.print_hand(hand)
                    self.set_result(2, hand_index)
                    if hand_index == num_splits: #if the player has bust on their last playable hand
                        return 
                    else: #if the player has more hands to play (from a split)
                        self.set_hand_index(hand_index+1)
                elif (len(hand) == 2) and hand[0][0] == "A":
                    self.print_hand(hand)
                    print("Hand over as you split aces.")
                    self.set_result(1, hand_index)
                    if hand_index == num_splits: #if the player has bust on their last playable hand
                        return 
                    else: #if the player has more hands to play (from a split)
                        self.set_hand_index(hand_index+1)
            elif action == "stand":
                self.set_result(1, hand_index)
                if hand_index == num_splits: #if the player has bust on their last playable hand
                    return 
                else: #if the player has more hands to play (from a split)
                    self.set_hand_index(hand_index+1)
            elif action == "split":
                #check if the player only has 2 cards in the hand they want to split
                if (len(hand) != 2):
                    print("You cannot split this hand.")
                    continue
                elif ((hand[0][0] != hand[1][0]) and (self.get_value(hand) != 20)):
                    print("You cannot split this hand.")
                    continue
                elif num_splits == 3:
                    print("you have already split the max amount of times.")
                    continue
                elif player.get_bet() > player.get_money():
                    print("You do not have enough money to split your hand.")
                    continue
                                
                #split the hand
                self.hand[hand_index]=[hand[0]]
                i=0
                while self.hand[hand_index+i] != []:
                    i+=1
                self.hand[hand_index+i]=[hand[1]]
                num_splits+=1
                self.set_has_split()
                self.set_money(-self.get_bet())
            elif action == "double down":
                #check if the player is allowed to double down
                if self.get_has_split():
                    print("You cannot double down after splitting.")
                    continue
                elif player.get_value(hand) == 21:
                    print("You cannot double down on 21.")
                    continue
                elif len(hand) != 2:
                    print("You can only double down with 2 cards.")
                    continue
                elif player.get_bet() > player.get_money():
                    print("You do not have enough money to split your hand.")
                    continue
                
                #player is able to double down, so they get one additional card
                #and their turn is over
                self.set_hand(pop_shoe(), hand_index)
                self.print_hand(hand)
                if self.get_value(hand) > 21: #player bust
                    self.set_result(2, hand_index)
                else: #player stood
                    self.set_result(1, hand_index)
                self.set_money(-self.get_bet())
                self.set_bet(self.get_bet()*2)
                return
            else:
                print("Error: command is invalid.")
    
    #get the data for if the player has split in this turn
    def get_has_split(self):
        return self.has_split

    #the player has split, set the data to 1
    def set_has_split(self):
        self.has_split = 1
    
    #get player total money
    def get_money(self):
        return self.money
    
    #increment player total money by the players bet size
    def set_money(self, bet):
        self.money += bet
    
    #get player bet size
    def get_bet(self):
        return self.bet_size
    
    #set player bet size
    def set_bet(self, bet):
        self.bet_size = bet
    


#begin creating the game
create_shoe()
print("Welcome to the world's best blackjack simulator!")

#ask for user to input the number of players (between 1 and 8 inclusive)
#also sanitize the input by verifying the input can be an integer and then 
#checking the value of the integer
while True:
    #get user input
    num_players = input("Please enter the number of players (between 1 and 8 players): ")
    try: #sanitize input
        num_players = int(num_players)
        if num_players < 1 or num_players > 8:
            print("Error: Please enter only a number between 1 and 8 for the number of players.")
        else: 
            break #input is valid stop asking for user input
    except (TypeError, ValueError):
        print("Error: Please enter only a number between 1 and 8 for the number of players.")
        
#create player objects for each guest and the house
players = []
Player1 = Guest("Player1")
players.append(Player1)
if num_players > 1:
    Player2 = Guest("Player2")
    players.append(Player2)
if num_players > 2:
    Player3 = Guest("Player3")
    players.append(Player3)
if num_players > 3:
    Player4 = Guest("Player4")
    players.append(Player4)
if num_players > 4:
    Player5 = Guest("Player5")
    players.append(Player5)
if num_players > 5:
    Player6 = Guest("Player6")
    players.append(Player6)
if num_players > 6:
    Player7 = Guest("Player7")
    players.append(Player7)
if num_players > 7:
    Player8 = Guest("Player8")
    players.append(Player8)
house = House("House")
players.append(house)


#the game has been (mostly) setup, so begin playing the game
while True:
    print()
    print("*** new hand ***")
    
    #reset the hands of each player from any previous turns
    for player in players:
        player.reset_hand()
        if player.get_name() != "House":
            #check if the player has enough money to place a bet, if not delete
            #all the data associated with the player. quit if no players left
            if player.get_money() <= 0:
                print(player.get_name(), "you are out of money and have been eliminated.")
                players.remove(player)
                del player
                if len(players) == 1:
                    print("all players have been eliminated. Now stopping the simulator.")
                    exit()
            while True:
                #get player bet size
                bet_size = input(str(player.get_name()) + " you have $" + str(player.get_money()) + " Please enter your bet size: ")
                try: #sanitize input
                    bet_size = int(bet_size)
                    if bet_size < 1 or bet_size > player.get_money():
                        print("Error: Please place a bet between 1 and", str(player.get_money()) + ".")
                    else: #input is valid stop asking for user input, set bet
                        player.set_money(-bet_size)
                        player.set_bet(bet_size)
                        break
                except (TypeError, ValueError):
                    print("Error: Please place a bet between 1 and", str(player.get_money()) + ".")
    
    #deal the cards
    for i in range(2):
        for player in players:
            card = pop_shoe()
            player.set_hand(card, player.get_hand_index())
    
    # print the cards in each players hand
    for player in players:
        if player.name != "House":
            player.print_hand(player.get_hand(player.get_hand_index()))
        else:
            player.print_hand_hidden()
    print()
    
    #have each player take their turn, each player plays until they stand or 
    #bust, house goes lasts and only plays if someone stood
    everyone_bust = 1
    for player in players:
        #have the player take an action
        if player.get_name() != "House":
            player.action() 
            for hand_index in range(player.get_hand_index()+1):
                if player.get_result(hand_index) == 1: #note if anyone did not bust
                    everyone_bust = 0
        elif not everyone_bust: #if someone did not bust have the house take its turn
            player.action()
        
    #check who has won, tied or lost
    #blackjack (an ace combined with any one of the following: K, Q, J, 10 
    #beats any 21 that isn't also blackjack)
    house_hand = house.get_hand(HOUSE_HAND_INDEX)
    house_value = house.get_value(house_hand)
    house_beat_all_first_print = 1
    for player in players:
        if everyone_bust:
            if  house_beat_all_first_print:
                print("everyone busted, dealer wins.")
                house_beat_all_first_print = 0
            continue
        if player.get_name() == "House": #skip the house
            break
        
        #for each hand the player has (in case of splits)
        for hand_index in range(player.get_hand_index()+1):
            hand = player.get_hand(hand_index)
            value = player.get_value(hand)
            if value > 21: #if the player busted
                print(player.get_name(), "has lost to the house with hand", str(hand_index+1) + ".")
            elif house_value > 21: #if the dealer busted
                print(player.get_name(), "has beat the house with hand", str(hand_index+1) + ".")
                player.set_money(player.get_bet()*2)
            elif value > house_value: #if the player beat the house
                print(player.get_name(), "has beat the house with hand", str(hand_index+1) + ".")
                player.set_money(player.get_bet()*2)
            elif value == house_value: # if the player has the same hand value
                #if the guest has blackjack and the dealer does not but has 21
                if len(hand) == 2 and len(house_hand) != 2 and value == 21: 
                    print(player.get_name(), "has beat the house with blackjack with hand", str(hand_index+1) + ".")
                    player.set_money(player.get_bet()*2)
                #if the house has blackjack and the guest does not but has 21
                elif len(house_hand) == 2 and len(hand) != 2 and value == 21: 
                    print(player.get_name(), "has lost to the house's blackjack with hand", str(hand_index+1) + ".")
                else:
                    print(player.get_name(), "has tied with the house with hand", str(hand_index+1) + ".")
                    player.set_money(player.get_bet())
            else:
                print(player.get_name(), "has lost to the house with hand", str(hand_index+1) + ".")