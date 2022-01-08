import random
import os # used to clear terminal when player is done with their turn
import time
from itertools import product
from art import title

class Card:
    def __init__(self,name,suit):
        self.name = name
        self.suit = suit

    def __repr__(self): # String representation for Card objects 
        return self.name + ' of ' + self.suit
# End Card Class

values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
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
cpu_hand = []

def game_setup(hand):
        name = input('Please enter your name: \n')
        print('\nWelcome',name +'!\n')
        print(name + '\'s hand:\n')
        for y in hand:
            print(y[0])
        return name

return_random_card = lambda x: x.pop([random.randint(0,len(x)-1)][0])
# Returns and removes a random card from the deck 
# def return_random_card():
#     num = random.randint(0,len(deck)-1)
#     removed = deck[num]
#     deck.remove(removed)
#     return removed

# Loop through for block 5 times, adding a card to each players hand with every iteration
# Only called at the beginning of the game 
def deal_cards():
    for x in range(0,5):
        # Remove a random card from the deck 
        dealt_card = return_random_card(deck)
        p1_hand.append(dealt_card)
        dealt_card = return_random_card(deck)
        cpu_hand.append(dealt_card)

# Random card from deck is removed and appended to player hand list 
def draw_card_from_deck(hand):
    try:

        if len(deck) == 0:
            print('Shuffling')
            time.sleep(1.5)
            deck[:] = discard
            discard[:] = [return_random_card(deck)]

    finally:
        drawn_card = return_random_card(deck)
        hand.append(drawn_card)




# Finds card based on user input, removes it from the deck, and inserts it to the front/top of the discard pile/list  
def play_card_from_hand(choice,hand):
    
    if hand[choice][0].name[0] == 8:
        #choice = crazy8()
        print(title)
        time.sleep(1.0)
        card_played = hand[choice]
        hand.remove(hand[choice])
        discard.insert(0,card_played)
        
    elif discard[0][0].name == hand[choice][0].name or discard[0][1] == hand[choice][1]:
        card_played = hand[choice]
        hand.remove(hand[choice])
        discard.insert(0,card_played)
    else: 
        os.system('cls' if os.name == 'nt' else 'clear')
        print('The card you played was',hand[choice],'That card does not match the suit or value of the top card.\nPlease try again')
        player_turn(hand)

def player_turn(hand):
    print('Cards in deck:',len(deck))
    if len(p1_hand) == 0:
        print('Game over')
        game = 0
    print('User is taking their turn.')
    print('Top card:',discard[0][0],'\n')

    for i,card in enumerate(hand):
        print(i,'--',card[0])
    print(len(hand),'-- Draw card')

    #try:
    choice = int(input('Which card would you like to play?\n'))
    if choice >= len(hand):
        draw_card_from_deck(hand)
        os.system('cls' if os.name == 'nt' else 'clear')
        player_turn(hand)
    else: play_card_from_hand(choice,hand) 
    # except: 
    #     #os.system('cls' if os.name == 'nt' else 'clear')
    #     print('Not a valid card choice')
    #     player_turn(hand,name)
        
# def playable_cpu():
#     for i in cpu_hand:
#           if discard[0][0].name == i[0].name or discard[0][1] == i[1]:
#               card = i
#               return card
#           else:
#               draw_card_from_deck(cpu_hand)
#               break
#     playable_cpu()
    

def computer_turn():
    print('Cards in deck:',len(deck))
    
    if len(cpu_hand) == 0:
        print('Computer wins')
        game = 0
    
    turn = 1
    print('Top card:',discard[0][0],'\n')
    while turn:
        print('Computer is picking a card...')
        count=0
        top_card = discard[0]
        string_top = str(top_card[0])
        
        for x in cpu_hand:
            print('Count',count)
            count+=1
            #stores card list object and turns 'name' into a string and slices out the first index of the string
            #i need first index to compare it to the discard pile first string index. stored in current_string to manipulate
            #adds current back in to cpu hand list
            #this also helps to identify the card that I need to grab and put into the discard pile  
            current = cpu_hand.pop()
            current_string = str(current[0])
            print(current_string,'Current')
            cpu_hand.insert(0,current)
            print(string_top[0],'==',current_string[0],'or',top_card[1],'==',current[1],'\n')
            if string_top[0] == current_string[0] or top_card[1] == current[1]:
                
                print('Found card\n')
                card_play = cpu_hand.pop(0)
                discard.insert(0,card_play)
                print(discard[0])
                return card_play
            # else:
            #     print('moving\n')
            #     backed = x
            #     cpu_hand.pop(x)
            #     cpu_hand.append(backed)
        print('game end')
        turn = 0
        # if 44 < 3:
        #     print('No card in hand')
            
        #     if len(deck) == 0:
        #             print('Shuffling')
        #             time.sleep(1.5)
        #             deck[:] = discard
        #             discard[:] = [return_random_card(deck)]
        #             continue
                    
            
        #     print('Drawing!.. #',count)
        #     count +=1
        #     num = random.randint(0,len(deck)-1)
        #     card = deck.pop(num)
        #     cpu_hand.append(card)
        #     print(card)
        #     print(cpu_hand)
        #     continue
        # else:
        #     print('Found one!!!!')
        #     deck.remove(deck[0])
        #     turn = 0
    # card = cpu_hand.pop(cpu_hand[0])
    # discard.insert(0, card)
    # print('Computer played',card[0])
    print(input('Press enter to take your turn.\n'))
    
        
    #check if hand contains a playable card
    #discard[0]
    #discard[0][0].name == hand[choice][0].name or discard[0][1] == hand[choice][1]:
    #if hand does not contain a playable card, then cpu draws card from deck
    #if hand does contain a playable card, remove from hand and append to discard
    

# GAME START


def main():
    print(title)
    time.sleep(1.0)
    # Removes 10 random cards from the deck and adds 5 to each players hand 
    deal_cards()
    discard.append(return_random_card(deck))

    name1 = game_setup(p1_hand)
    print(input('\nPress Enter to start the game!\n'))
    os.system('cls' if os.name == 'nt' else 'clear')
    
    game = 1
    while game:
        # player_turn(p2_hand,name2)
        # if len(p2_hand) == 0:
        #     game = 0
        # os.system('cls' if os.name == 'nt' else 'clear')
        # print(input('\nPress Enter to proceed to Player 1\'s turn\n'))
        

        computer_turn()
        player_turn(p1_hand)
        
        
        
        # End of game loop

print('\n')
main()