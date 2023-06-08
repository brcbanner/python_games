'''
Finding the most "correct" word of a wrong 
word using the division into trigrams
'''

def trigrams(s):
    trigs = []
    for i in range(1, len(s)-1):
        string = ''
        string += s[i-1] + s[i] + s[i+1]
        trigs.append(string)
    return trigs

#print(trigrams('abbazlio'))
#print(trigrams('abbaglio'))
#print(trigrams('abbazia'))

def similarity_trigrams(w1, w2):
    x = trigrams(w1)
    y = trigrams(w2)
    while len(x) != len (y):
        if len(x) < len(y):
            x.append('')
        else:
            y.append('') 
    count = 0
    for c in range(len(x)):
        if x[c] == y[c]:
            count += 1
    return count/len(x)

#print(similarity_trigrams('abbazlio', 'abbaglio'))
#print(similarity_trigrams('abbazlio', 'abbazia'))

def correct_word_trigrams(s):
    f = open('parole_italiane_short.txt')
    value = 0
    w = ''
    for word in f:
        number = similarity_trigrams (s, word)
        if number > value:
            value = number
            w = word
    return w

s = 'botticlia'
print(f"The correct word with the trigram method for {s} is: {correct_word_trigrams(s)}")

'''
Finding the most "correct" word of a wrong 
word using the division into single letters
'''

def sng_lets(s):
    sng_lets_list = []
    for i in s:
        sng_lets_list.append(i)
    return sng_lets_list

#print(sng_lets('abbazlio'))
#print(sng_lets('abbaglio'))
#print(sng_lets('abbazia'))


def similarity_sng_lets(w1, w2):
    x = sng_lets(w1)
    y = sng_lets(w2)
    while len(x) != len (y):
        if len(x) < len(y):
            x.append('')
        else:
            y.append('') 
    count = 0
    for c in range(len(x)):
        if x[c] == y[c]:
            count += 1
    return count/len(x)

#print(similarity_sng_lets('abbazlio', 'abbaglio'))
#print(similarity_sng_lets('abbazlio', 'abbazia'))

def correct_word_sng_lets(s):
    f = open('parole_italiane_short.txt')
    value = 0
    w = ''
    for word in f:
        number = similarity_sng_lets (s, word)
        if number > value:
            value = number
            w = word
    return w

s = 'botticlia'
print(f"The correct word with the single letters method for {s} is: {correct_word_sng_lets(s)}")