'''
Josephus problem with binary numbers
(link to the explanation of the method: https://www.youtube.com/watch?v=uCsD3ZGzMgE)
'''

# conversion of a number N from decimal base to binary base
def conv_10_2(n):
    
    # it calculates the exp of power 2 of the nearest number greater than N
    # e.g. pow_2(18) --> 4
    # this function is useful for understanding the number of bits to
    # represent N in base 2
    def pow_2(number): 
        p = 0
        while number > 0:
            number = number // 2
            p += 1
        return p
    
    n_bits = pow_2(n)
    
    # conversion from N base 10 to list containing N base 2 (N_bas_2)
    # e.g.  5 (base 10) --> [1, 0, 1] (base 2)
    N_bas_2 = []
    for i in range (n_bits):
        if n % 2 == 1:
            N_bas_2.append(1)
        else:
            N_bas_2.append(0)
        n = n // 2
    
    # list inversion
    new_N_bas_2 = []
    for z in range(n_bits):
        new_N_bas_2.append(N_bas_2[-z-1])
        
    return new_N_bas_2
        
# opposite conversion of conv_10_2
def conv_2_10(list_n_bin):
    u = 0
    for i in range (1, len(list_n_bin)+1):
        u += list_n_bin[-i] * 2**(i-1)
    return u

def safe_1(N):
    w = 0
    n_bin = conv_10_2(N)
    w = n_bin[0]
    n_bin.pop(0)
    n_bin.append(w)
    return (conv_2_10(n_bin))

'''
Josephus problem with 'brute force'/'by hand'
'''

def safe_2(N):
    players = list(range(1, N+1))
    alive = len(players)
    while alive > 2:
        if alive % 2 == 0:
            players = players[::2]
            alive = len(players)
        else:
            players = players[::2]
            players.pop(0)
            alive = len(players)
    return players[0]






