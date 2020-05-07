from numpy.random import seed
from numpy.random import shuffle
import numpy as np
import random

def lab():
    k=25
    sq1 = np.arange(25,34)
    sq1 = np.resize(sq1,(3,3))
    for i in sq1:
        for j in range(3):
            i[j] = k
        k+=1
    return sq1


def process_s(sequence):
    news= ""
    for i in sequence:
        if i != '[' and i != ']' and i != ',':
            news +=str(i)+" "
    news = news.split()
    news =  list(map(int,news))

def ch(sequence):
    k=0
    dummy = np.zeros(17, dtype=np.int64)
    sequence = np.concatenate((sequence,dummy)).tolist()
    la = lab().tolist()
    sq = []
    while len(sq) < 3:
        # print(sequence)
        k = random.randint(0,32)
        if k%7 <2 and k//6 not in sq:
            sq.append(k//6)
            for i in range(3):
                sequence.insert(k,la[len(sq)-1][0])
    return str(sequence)

def process_string(sequence):
    news= ""
    for i in sequence:
        if i != '0' and i != '[' and i != ']' and i != ',':
            news +=i
    return news.split()


# seed(1)
def gentable():
    #42
    sequence = np.arange(1,26)
    shuffle(sequence)
    shuffle(sequence)
    shuffle(sequence)
    shuffle(sequence)
    for i in range(25):
        sequence[i] = sequence[i]//5 + 1
    s = ch(sequence)
    sequence = process_string(s)
    for i in range(8):
        sequence.append('0')
    table = np.resize(sequence,(6,7))
    return table
    # lp = np.arange(42,48)
    # shuffle(lp)
    # lp = np.reshape(lp,(6,1))
    # table = np.hstack((table,lp ))
    # return table



def add_freep(table):
    x = np.array(['free'])
    for i in range(5):
        x = np.append(x, ['free'])
    x = np.resize(x,[6,1])
    table = np.hstack((table,x))
    return table


def ran(r):
    return random.randint(0,r)