from deck import Deck
from money import money

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def get_hand_value(self):
        hand_value = 0
        num_aces = 0
        for value, _ in self.hand:
            if value.isdigit():
                hand_value += int(value)
            elif value in ['Jack', 'Queen', 'King']:
                hand_value += 10
            else:  # Ace
                hand_value += 11
                num_aces += 1
        while hand_value > 21 and num_aces > 0:
            hand_value -= 10
            num_aces -= 1
        return hand_value

class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")

    def reveal_first_card(self):
        print(f"Dealer's hand: [{self.hand[0]}]")

class BlackjackGame:
    def __init__(self, num_players):
        self.num_players = num_players
        self.deck = Deck()
        self.players = [Player(f"Player {i+1}") for i in range(num_players)]
        self.dealer = Dealer()
        self.bet_manager = money()

    def deal_initial_cards(self):
        for _ in range(2):
            for player in self.players + [self.dealer]:
                player.add_card(self.deck.deal(1)[0])

    def display_hands(self, reveal_dealer_card=False):
        print("Dealer's hand:")
        if reveal_dealer_card:
            for card in self.dealer.hand:
                print(f"[{card}]")
        else:
            print("[Hidden Card]", f"[{self.dealer.hand[1]}]")
        print("\nPlayers' hands:")
        for player in self.players:
            print(f"{player.name}: {[card for card in player.hand]}")

    def play_round(self):
        self.deal_initial_cards()
        self.display_hands(reveal_dealer_card=False)

        for player in self.players:
            while True:
                decision = input(f"{player.name}, do you want to hit or stand? (h/s): ").lower()
                if decision == 'h':
                    player.add_card(self.deck.deal(1)[0])
                    self.display_hands(reveal_dealer_card=False)
                    if player.get_hand_value() > 21:
                        print(f"{player.name} busts!")
                        break
                elif decision == 's':
                    break
                else:
                    print("Invalid choice. Please enter 'h' or 's'.")

        self.dealer.reveal_first_card()
        while self.dealer.get_hand_value() < 17:
            self.dealer.add_card(self.deck.deal(1)[0])
            print("Dealer hits.")
            self.display_hands(reveal_dealer_card=True)

        dealer_hand_value = self.dealer.get_hand_value()
        for player in self.players:
            player_hand_value = player.get_hand_value()
            if player_hand_value > 21:
                print(f"{player.name} busts!")
            elif dealer_hand_value > 21 or player_hand_value > dealer_hand_value:
                print(f"{player.name} wins!")
                self.bet_manager.win(player.name, player.bet(0) * 2)
            elif player_hand_value == dealer_hand_value:
                print(f"{player.name} ties with the dealer.")
                self.bet_manager.win(player.name, player.bet(0))
            else:
                print(f"{player.name} loses.")
        
    def play_game(self):
        while True:
            self.play_round()
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != 'y':
                break

if __name__ == "__main__":
    num_players = int(input("Enter number of players: "))
    game = BlackjackGame(num_players)
    game.play_game()
