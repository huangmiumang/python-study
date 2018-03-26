import random
import itertools

def deal(numhands, n = 5, deck = [r + s for r in '23456789TJQKA' for s in 'SHDC']):
    random.shuffle(deck)
    return [deck[n * i : n * (i + 1)] for i in range(numhands)]

def hand_percentages(n = 700 * 1000):
    counts = [0] * 9
    hand_name = ["Straight Flush", "4 of a Kind",
                 "Full House", "Flush", "Straight",
                 "3 of a Kind", "2 Pair", "Pair", "High Card"]
    for i in range(n / 10):
        for hand in deal(10):
            ranking = hand_rank(hand)[0]
            counts[ranking] += 1
    for i in reversed(range(9)):
        print "%14s: %6.3f %%" % (hand_name[i], 100.*counts[i] / n)

def poker(hands):
    print "result"
    print allmax(hands, key = hand_rank)
    return max(hands, key = hand_rank)

def allmax(iterable, key = None):
    result, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)
    return result

def best_hand(hand):
    return max(itertools.combinations(hand, 5), key = hand_rank):

def test_best_hand():
    assert(sorted(best_hand("6C 7C 8C 9C TC 5C JS".split())) 
           == ['6C', '7C', '8C', '9C', 'TC'])
    assert(sorted(best_hand("TD TC TH 7C 7D 8C 8S".split())) 
           == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert(sorted(best_hand("TD TC TH 7C 7D 8C 8S".split())) 
           == ['7C', '7D', '7H', '7S', 'TD'])
    return 'test_best_hand pass'

def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)

def card_ranks(hand):
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    if ranks == [14, 5, 4, 3, 2]:
        return [5, 4, 3, 2, 1]
    else:
        return ranks

def straight(ranks):
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5

def flush(hand):
    suits = [s for r, s in hand]
    return len(set(suits)) == 1

def kind(n, ranks):
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None

def two_pair(ranks):
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None

def test():
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    tp = "5S 5D 9H 9C 6S".split()
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] +99 * [fh]) == sf
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    return "test pass"

#print test()
#print deal(2)
#hand_percentages()
print test_best_hand()
