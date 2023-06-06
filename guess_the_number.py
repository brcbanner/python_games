''' Ex. 1 '''
# Guess a random number 'choosen by computer' between 1 and n

import random

def guess_number_choose_by_computer(n):
    random_number_choose_by_comp = random.randint(1,n)
    guess = 0
    while random_number_choose_by_comp != guess:
        guess = int(input('New attempt: '))
        if guess > random_number_choose_by_comp:
            print ('Oops, your number is incorrect. You are too high! ')
        elif guess < random_number_choose_by_comp:
            print ('Sorry, your number is incorrect. You are too low! ')
    print (f'Congrats!! The number {guess} is correct')


''' Ex. 2 '''
# Computer tries to guess your number which you have choosen between 1 and n

def guess_number_choose_by_user(n):
    feedback = ''
    low = 1
    high = n
    while feedback != 'c':
        random_number_choose_by_computer = random.randint(low, high)
        feedback = input(f'Is {random_number_choose_by_computer} too high (h), too low (l) or correct (c)? ')
        if feedback == 'h':
            high = random_number_choose_by_computer
        elif feedback == 'l':
            low = random_number_choose_by_computer
    print("YeAh, I'm SmArT")