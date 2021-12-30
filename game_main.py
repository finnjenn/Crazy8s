# a deck needs a way to shuffle , a way to remove items, a draw_card_from pile , a way to reset deck
# when the deck runs out , it needs to be able to access the discard , shuffle its contents , and add it to the deck 
# it needs to be able to distribute the same amount of cards to each player (doesnt matter if its two players)
# cards need a name , suit , value
# code old maid or crazy eights 
# store count of cards in players hands into a variable. if it reaches zero, player has won 
# i need some way to store each player's current hand separately 
# i need to check the top of the 'discard' and see if it matches the card that the user placed. 
# if it doesnt match, I need to reset player turn and ask them try pick a card that matches in suit or value 
# if a player doesnt have a card, have them pick draw_card_from (or maybe just force the draw_card_from) until they have a card that can be placed
import random
import os # used to clear terminal when player is done with their turn
#os.system('cls' if os.name == 'nt' else 'clear')

class Card:
    def __init__(self,name,suit):
        self.name = name
        self.suit = suit

    def __repr__(self): # String representation for Card objects 
        return self.name + ' of ' + self.suit
# End Card Class

values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
suites = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

# Using list comphrehenion, creates a list containing [card object, value of suit] -- Ex. -- [[2 of Hearts, 0] , [2 of Clubs, 1] , [2 of Diamonds, 2] , [2 of Spades, 3] , [3 of Hearts, 0]] etc. for every card
# Similar to using nested for loops to match each value of values to a suit in suites
deck = [[Card(v,s),i] for v in values for i,s in enumerate(suites)]

# VALUE OF SUITS
# Hearts = 0
# Clubs = 1
# Diamonds = 2
# Spades = 3

# ORIGINAL CODE THAT INSPIRED MY LIST COMPREHENSION
# deck = [[v + ' of ' + s,s] for v in values for s in suites]


discard = []
p1_hand = []
p2_hand = []

# Returns and removes a random card from the deck 
def return_random_card():
    num = random.randint(0,len(deck)-1)
    removed = deck[num]
    deck.remove(removed)
    return removed

# Random card from deck is removed and appended to player hand list 
def draw_card_from_deck(hand):
    removed_card = return_random_card()
    hand.append(removed_card)

# Loop through for block 5 times, adding a card to each players hand with every iteration
# Only called at the beginning of the game 
def deal_cards():
    for x in range(0,5):
        # Remove a random card from the deck 
        dealt_card = return_random_card()
        p1_hand.append(dealt_card)
        dealt_card = return_random_card()
        p2_hand.append(dealt_card)

# Finds card based on user input, removes it from the deck, and inserts it to the front/top of the discard pile/list  
def play_card_from_hand(choice,hand):
    if discard[0][0].name == hand[choice][0].name or discard[0][1] == hand[choice][1]:
        card_played = hand[choice]
        hand.remove(hand[choice])
        discard.insert(0,card_played)
    else: 
        os.system('cls' if os.name == 'nt' else 'clear')
        print('That card does not match the suit or value of the top card.\nPlease try again')
        player_turn(hand)

def player_turn(hand):
    print('Top card:',discard[0][0],'\n')

    for i,card in enumerate(hand):
        print(i,'--',card[0])
    print(len(hand),'-- Draw card')

    try:
        choice = int(input('Which card would you like to play?\n'))
        if choice == len(hand):
            draw_card_from_deck(hand)
            os.system('cls' if os.name == 'nt' else 'clear')
            player_turn(hand)
        else: play_card_from_hand(choice,hand) 
    except: 
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Not a valid card choice')
        player_turn(hand)



# GAME START
# Removes 10 random cards from the deck and adds 5 to each players hand 
deal_cards()

# Player 1 inputs information for their name
name1 = input('\nPlayer 1. Please enter your name: \n')
print('\nWelcome',name1 +'!\n')

# Show player 1 their hand
print(name1 + '\'s hand:\n')
for i,x in enumerate(p1_hand):
    print(p1_hand[i][0])

# Pauses program to allow Player 1 to view their hand
print(input('\nPress Enter to input a name for Player 2\n'))
    
# clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# Player 2 inputs information for their name
name2 = input('Player 2. Please enter your name: \n')
print('\nWelcome',name2 +'!\n')

# Show player 2 their hand
print(name2 + '\'s hand:\n')
for i,x in enumerate(p2_hand):
    print(p2_hand[i][0])

# Pauses program to allow Player 2 to view their hand
print(input('\nPress Enter to begin game!\n'))
    
# clear screen and begin game
os.system('cls' if os.name == 'nt' else 'clear')

# Returns and removes a random card called starter_card from the deck and adds it to discard 
starter_card = return_random_card()
discard.append(starter_card)
# This card is the first card in the discard pile and it is 'face-up' to be viewed by the first player to take their turn


   

game = 1
while game:
    #Player 1 turn loop variable
    player_turn(p1_hand)
    if len(p1_hand) == 0:
        game = 0
    player_turn(p2_hand)
    if len(p2_hand) == 0:
        game = 0
    

    
    # End of game loop