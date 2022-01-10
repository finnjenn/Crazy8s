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
        return self.name_value
    
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
values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
suites = ['Hearts', 'Clubs', 'Diamonds', 'Spades']    
deck = [Card(value,suit,suit_value) for value in values for suit_value,suit in enumerate(suites)]
discard_pile = []
user_cards = []
computer_cards = []
    
return_random_card = lambda game_deck: game_deck.pop([random.randint(0,len(game_deck)-1)][0])
flip_top_card = lambda discard: discard.append(return_random_card(deck))

def is_valid_card(card):
    top_card = discard_pile[0]
    if card.get_first_character() == 8:
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
        
def draw_card_from_deck(player_hand):
    '''Appends a random card into the user's hand.
    Unless the deck list is empty. Then it would shuffle the discard into deck first.'''
    if len(deck) == 0:
        shuffle_discard_into_deck()
    else:player_hand.append(return_random_card(deck))
    
def play_card_from_hand(hand,choice):
    '''Compares the card that the user selected to the top card in the discard pile to validate if the card is legally playable.
    If so, removes the card from the user's hand and inserts it as the top card in the discard pile.
    If not, lets the user know that the card is not playable and retriggers their turn.'''
    user_chosen_card = hand[choice]
    
    if is_valid_card(user_chosen_card):
        hand.remove(user_chosen_card)
        discard_pile.insert(0,user_chosen_card)
       
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('The card you played was',user_chosen_card,'\nThat card does not match the suit or value of the top card.\nPlease try again.')
        user_take_turn()  
             
def game_setup():
    deal_cards()
    flip_top_card(discard_pile)  

    
def computer_take_turn():
    print('Computer is picking a card...')
    
    for current_card in computer_cards:
        if is_valid_card(current_card):
            discard_pile.insert(0,current_card)
            computer_cards.remove(current_card)
            time.sleep(1.5)
            print('The computer picked', current_card)
            return
    print('Computer needs to draw a card.')
    draw_card_from_deck(computer_cards)
    computer_take_turn()
                
def user_take_turn():
    pass

def main():
    game_setup()
    print(computer_cards)
    computer_take_turn()
main()