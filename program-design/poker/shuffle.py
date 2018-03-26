#!/usr/bin/python
#coding=utf-8

import random
import collections

def deal(numhands, n = 5, deck = [r + s for r in '23456789TJQKA' for s in 'SHDC']):
    random.shuffle(deck)
    return [deck[n * i : n * (i + 1)] for i in range(numhands)]

#可能会导致死循环
def shuffle1(deck):
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = swapped[j] = True
        swap(deck, i, j)

def shuffle2(deck):
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = randrange(N), randrange(N)
        swapped[i] = True
        swapped(deck, i, j)

def shuffle3(deck):
    N = len(deck)
    for i in range(N):
        swap(deck, i, randrange(N))

def shuffle(deck):
    N = len(deck)
    for i in range(N - 1):
        swap(deck, i, random.randrange(i, N))

def swap(deck, i, j):
    deck[i], deck[j] = deck[j], deck[i]

def test_shuffler(shuffler, deck = 'abcd', n = 10000):
    counts = collections.defaultdict(int)
    for _ in range(n):
        input = list(deck)
        shuffler(input)
        counts[''.join(input)] += 1
    e = n * 1./factorial(len(deck))
    ok = all((0.9 <= counts[item] / e <= 1.1) for item in counts)
    name = shuffler.__name__
    print '%s(%s) %s' % (name, deck, ('ok' if ok else '*** BAD ***'))
    print '\t',
    for item, count in sorted(counts.items()):
        print "%s:%4.lf" % (item, count * 100./n)
    print

def factorial(n):
    return 1 if (n <= 1) else n * factorial(n - 1)

def test_shufflers(shufflers = [shuffle, shuffle1], decks = ['abc', 'ab']):
    for deck in decks:
        print
        for f in shufflers:
            test_shuffler(f, deck)

test_shufflers()
