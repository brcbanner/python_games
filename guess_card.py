# Guess a card in a deck

import random

def guess_card(n):
    # explanation of game
    print("""You vs Computer
Pick any card from any of the three decks, and for each turn (for a total of 
3 turns) you will need to tell your computer in which deck is the same card 
you chose at the beginning of the game.
Let's play!!""")
   
    cards_each_deck = n//3
    numbers_figures = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', 'jack', 'queen','king']
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
   
    l1, l2, l3 = [], [], []
    k = []
    for _ in range(3):
        u = 0
        while u < cards_each_deck :
            x = random.choice(numbers_figures).upper()
            y = random.choice(suits).upper()
            s = x + '_' + y
            if len (l1) < cards_each_deck and s not in k :
                l1.append(s)
                k.append(s)
                u += 1
            elif len (l2) < cards_each_deck and s not in k:
                    l2.append(s)
                    k.append(s)
                    u += 1
            elif s not in k:
                    l3.append(s)
                    k.append(s)
                    u += 1
    i = 0
    while i < 3:
        print(f"DECK 1: {l1}")
        print(f"DECK 2: {l2}")
        print(f"DECK 3: {l3}")
        l = []
        n_deck = input("Which deck of three is your card in? (Type the number of the deck; e.g. first deck = 1) ")
        if n_deck == '1':
            l = l2 + l1 + l3
        elif n_deck == '2':
            l = l1 + l2 + l3
        else: 
            l = l1 + l3 + l2
        l1, l2, l3 = [], [], []
        for t in range (cards_each_deck):
            l1.append(l[3*t])
            l2.append(l[3*t+1])
            l3.append(l[3*t+2])
        i += 1
    
    print(f"Your card is: {l2[(cards_each_deck)//2]}")
