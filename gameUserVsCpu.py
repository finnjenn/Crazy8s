import random
import os
#os.system('cls' if os.name == 'nt' else 'clear')
import time
from art import title

def crazy_8_is_played():
    '''Signifies that a player has used a crazy 8. Prints crazy 8 title art from art.py.
    Sleep system for 1.5 seconds to keep art on screen. Finally clear the terminal'''
    print(title)
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')

class Card:
    def __init__(self,name_value,suit,suit_value):
        self.name_value = name_value
        self.suit = suit
        self.suit_value = suit_value
        
    def __repr__(self):
        '''Returns card string as "{value} of {suit}"
        Ex. "Queen of Diamonds"'''
        return self.name_value + ' of ' + self.suit
        
    def get_first_character(self):
        '''Returns the first character in the card name string.
        The character is used to compare against other cards characters to see if they match'''
        return self.name_value[0]
    
    def get_suit_value(self):
        '''Returns the suit value of the card.
        The suit value is used to compare against other cards suit value to see if they match'''
        return self.suit_value
# VALUE OF SUITS
# Hearts = 0
# Clubs = 1
# Diamonds = 2
# Spades = 3
# Using list comphrehenion, creates a list containing [card object, value of suit] -- Ex. -- [[2 of Hearts, 0] , [2 of Clubs, 1] , [2 of Diamonds, 2] , [2 of Spades, 3] , [3 of Hearts, 0]] etc. for every card
values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
suites = ['Hearts', 'Clubs', 'Diamonds', 'Spades']    
deck = [Card(value,suit,suit_value) for value in values for suit_value,suit in enumerate(suites)]
discard_pile = []
user_cards = []
computer_cards = []

# pops an item from deck at a random index and returns that object
return_random_card = lambda game_deck: game_deck.pop([random.randint(0,len(game_deck)-1)][0])

# appends a random card from the deck into the empty discard pile
# simulates picking the top card off of the deck to start the game
flip_top_card = lambda discard: discard.append(return_random_card(deck))

def is_valid_card(card):
    '''Returns True or False depending on whether or not the card is playable'''
    top_card = discard_pile[0]
    
    if card.get_first_character() == '8':
        crazy_8_is_played()
        return True
    
    elif card.get_first_character() == top_card.get_first_character() or card.get_suit_value() == top_card.get_suit_value():
        return True
    else:
        return False   
     
def shuffle_discard_into_deck():
    '''The empty deck list is set equal to the discard pile.
    A slice of all of the values in discard is set equal to and random card from the deck.'''
    print('Shuffling')
    time.sleep(1.5)
    deck[:] = discard_pile
    discard_pile[:] = [return_random_card(deck)]
    
def deal_cards():
    '''Appends a random card from the deck into the user's and the computer's hand 5 times in a loop '''
    for x in range(0,5):
        user_cards.append(return_random_card(deck))
        computer_cards.append(return_random_card(deck))
        
def draw_card_from_deck(hand):
    '''Appends a random card into the user's hand.
    Unless the deck list is empty. Then it would shuffle the discard into deck first.'''
    if len(deck) == 0:
        shuffle_discard_into_deck()
    else:hand.append(return_random_card(deck))


def display_cards(user_cards):
    '''Takes in the user's hand as an argument and displays the cards'''
    print('0   --  Draw card')
    for i,card in enumerate(user_cards):
        print(i+1,'  -- ',card)
  
def play_card_from_hand(hand,choice):
    '''Compares the card that the user selected to the top card in the discard pile to validate if the card is legally playable.
    If so, removes the card from the user's hand and inserts it as the top card in the discard pile.
    If not, lets the user know that the card is not playable and retriggers their turn.'''
    user_chosen_card = hand[choice-1]
    
    if is_valid_card(user_chosen_card):
        hand.remove(user_chosen_card)
        discard_pile.insert(0,user_chosen_card)
       
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('The card you played was',user_chosen_card,'\nThat card does not match the suit or value of the top card.\nPlease try again.')
        user_take_turn(hand)  

def selection_screen(hand):
    '''Creates the text to show the user their selection options at the beginning of their turn'''             
    print('Top card:',discard_pile[0],'\n')
    time.sleep(1.25)
    print('The computer has',len(computer_cards),'cards left in its hand')

    print('Your hand:\n')
    time.sleep(1.5)
    display_cards(hand)
    
def game_setup():
    '''Calls deal_cards to put 5 cards in the user's and computer's hand.
    Calls flip top card to 'initialize' the game.
    Lets the user know that the computer will take the first turn of the game'''
    deal_cards()
    flip_top_card(discard_pile) 
    print('The computer will go first!\n') 

def computer_take_turn():
    '''Searches through computer_cards to find a valid card.
    If it finds one, it removes the card and inserts it into the first slot.
    If not, the user is notified that the computer is drawing a card and then it restarts the computer turn to begin searching again.'''
    time.sleep(1.5)
    for current_card in computer_cards:
        
        if is_valid_card(current_card):
            discard_pile.insert(0,current_card)
            computer_cards.remove(current_card)
            print('The computer picked', current_card,'\n')
            print(input('Press Enter to begin your turn\n'))
            os.system('cls' if os.name == 'nt' else 'clear')
            return
        
    print('Computer needs to draw a card.\n')
    draw_card_from_deck(computer_cards)
    computer_take_turn()
                
def user_take_turn(hand):
    '''Asks user which card they would like to play based on the text in selection_screen.
    If they select 0 -- Draw card, run draw_card_from_deck function, clear the screen and re run the user's turn.
    If a valid number based off of the selection screen is picked by the user, notify them which card they have played and wait for input from user to begin computer's turn'''
    selection_screen(hand)
    choice = int(input('\nWhich card would you like to play?\n'))
    
    if choice == 0:
        draw_card_from_deck(hand)
        os.system('cls' if os.name == 'nt' else 'clear')
        user_take_turn(hand)
        
    elif choice <= len(hand)+1:
        print('You played the',hand[choice-1])
        play_card_from_hand(hand,choice) 
        print(input('Press Enter to start Computer\'s turn\n'))
        os.system('cls' if os.name == 'nt' else 'clear')
    
    else: 
        print('Not a valid card choice')
        user_take_turn(hand)
        
def main():
    
    game_setup()
    
    while True:
        print('Top card:',discard_pile[0])
        
        computer_take_turn()
        
        if len(computer_cards) == 0:
            print('The computer is out of cards! You lost.')
            break 
          
        user_take_turn(user_cards)
        
        if len(user_cards) == 0:
            print('You used up all of your cards! Congratulations you won the game!')
            break
# End of main
main()