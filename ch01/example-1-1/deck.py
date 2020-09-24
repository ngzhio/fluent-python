import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                                        for suit in self.suits]
    
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

'''Playing with FrenchDeck

>>> deck = FrenchDeck()
>>> len(deck)
52
>>> deck[0]
Card(rank='2', suit='spades')
>>> deck[-1]
Card(rank='A', suit='hearts')
>>> from random import choice
>>> choice(deck)
Card(rank='4', suit='spades')
>>> choice(deck)
Card(rank='2', suit='spades')
>>> deck[:3]
[Card(rank='2', suit='spades'), Card(rank='2', suit='diamonds'), Card(rank='2', suit='clubs')]

'''
