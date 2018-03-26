import itertools

allranks = '23456789TJQKA'
redcards = [r + s for r in allranks for s in 'SC']
blackcards = [r + s for r in allranks for s in 'SC']

def best_wild_hand(hand):
    hands = set(best_hand(h)
                for h in itertools.product(*map(replacements, hand)))
    return max(hands, key = hand_rank)

def replacements(card):
    if card == '?B':
        return blackcards
    elif card == '?R':
        return recards
    else:
        return [card]
