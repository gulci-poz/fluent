import collections
from random import choice

# dunders - magic methods, framework methods

# klasa do reprezentacji talii
# obiekty nie mogą posiadać własnych metod
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for rank in self.ranks
                       for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()
print('lenth:', len(deck))
print(deck[33])
print(deck[-1])
print(deck[len(deck) - 1])
print('random picks')
print(choice(deck))
print(choice(deck))
print(choice(deck))
# dzięki odczytywaniu pozycji za pomocą implementacji __getitem__ możemy korzystać ze slicingu
print(deck[:3])
print(deck[12::13])
# dzięki temu deck jest również iterable
for card in deck:  # doctest: +ELLIPSIS
    print(card)
for card in reversed(deck):  # doctest: +ELLIPSIS
    print(card)
# mamy iterable, inaczej jeśli nie ma metody __contains__ to in robi skanowanie sekwencyjne
print(Card('Q', 'hearts') in deck)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card_obj):
    rank_value = FrenchDeck.ranks.index(card_obj.rank)
    return rank_value * len(suit_values) + suit_values[card_obj.suit]

for card in sorted(deck, key=spades_high):  # doctest: +ELLIPSIS
    print(card)
