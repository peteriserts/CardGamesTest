from deck import Deck
from money import money

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def show_hand(self):
        print(f"{self.name}'s hand: {[card for card in self.hand]}")

class Dealer:
    def __init__(self):
        self.hand = []

    def deal_initial_cards(self, players, deck):
        for _ in range(2):
            for player in players:
                player.add_card(deck.deal(1)[0])
            self.add_card(deck.deal(1)[0])

    def add_card(self, card):
        self.hand.append(card)

    def show_hand(self):
        print(f"Dealer's hand: {[card for card in self.hand]}")

class PokerGame:
    def __init__(self, num_players):
        self.num_players = num_players
        self.deck = Deck()
        self.players = [Player(f"Player {i+1}") for i in range(num_players)]
        self.dealer = Dealer()
        self.bet_manager = money()

    def deal_initial_cards(self):
        self.dealer.deal_initial_cards(self.players, self.deck)

    def display_hands(self):
        for player in self.players:
            player.show_hand()
        self.dealer.show_hand()

    def play_round(self):
        self.deal_initial_cards()
        self.display_hands()

    def play_game(self):
        self.play_round()

if __name__ == "__main__":
    num_players = int(input("Enter number of players: "))
    game = PokerGame(num_players)
    game.play_game()
