import random

class Deck:
    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [(value, suit) for _ in range(num_decks) for suit in self.suits for value in self.values]
        self.cut_percentage = 0.5
        self.stop_point = None

    def shuffle(self):
        random.shuffle(self.cards)

    def cut(self, percentage):
        if percentage < 0 or percentage > 1:
            raise ValueError("Percentage must be between 0 and 1")
        index = int(len(self.cards) * percentage)
        self.cards = self.cards[-index:] + self.cards[:-index]

    def set_stop_point(self, percentage):
        if percentage < 0 or percentage > 1:
            raise ValueError("Percentage must be between 0 and 1")
        index = int(len(self.cards) * percentage)
        self.cards.insert(index, ('Stop', 'Card'))

    def deal(self, num_cards):
        if self.stop_point is not None and ('Stop', 'Card') in self.cards:
            stop_index = self.cards.index(('Stop', 'Card'))
            dealt_cards = self.cards[:stop_index]
            self.cards = self.cards[stop_index:]
        else:
            dealt_cards = self.cards[:num_cards]
            self.cards = self.cards[num_cards:]
        return dealt_cards