# Hangman

import random

def hangman():
    
    # explanation of the game
    print ("""HANGMAN!!
You VS Computer
Guess the following word:""")
    
    # I take a random word 'y' from file 'parole_italiane_short.txt';
    # this wile be the word to guess
    x = open('parole_italiane_short.txt') # this file contains a list of many italian words
    y = random.choice(x.readlines())
    
    # the random string taken from the file contains, in addition to
    # its own characters, a last character '\n'; so...
    y = y[:-1]
    
    # then I want the word which will be shown on the screen to be
    # all uppercase
    y = y.upper()
    
    # I create a list 'l' to contain letters found in the word and
    # a string 's' representing the list with new type 'string'
    l = [] 
    for _ in y: 
        l.append('-')
    s = ''.join(l)
    print(s)
    
   
    # then I create a string 't' containing the letters that user tried
    t = ''
    
    while s != y:
        
        print (f"\nTried letters: {t}")
        z = input("\nNew letter: ")
        
        # I check if the capital letter 'z' is found and if 
        # this letter is not contained in the string 't': if the 
        # condition is true I print the string 's' previous but with 
        # the found letter inside
        if z.upper() in y and z not in t:
            for i in range(len(y)):
                if z.upper() == y[i]:
                    l[i] = z
            s = ''.join(l)
            s = s.upper()
            print (f'\nWord: {s}')
            
            # I update the string 't' with the tried letter 'z'
            t += z
        
        # I insert a new condition in case the user wants to leave the 
        # game; then I print the word 
        elif z == '0':
            print(f"\n_I'm sorry but you did not guess the word {y}_")
        
        # I insert the condition in which the tested letter has already 
        # been called
        elif z in t:
            print("\n_This letter has already been used_")
            
        # if it is not found then I print the previous 's'
        else:
            s = ''.join(l)
            s = s.upper()
            print (f'\nParola: {s}')
            
            # I update the string 't' with the tried letter 'z'
            t += z
        
    # in case the string ’s' is equal to the word to guess...
    print('\n__Hai indovinato la parola!__')