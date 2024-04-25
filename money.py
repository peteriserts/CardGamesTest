class money:

    def __init__(self):
        self.chips = 500  # Starting with 500 chips

    def get_chips(self):
        return self.chips

    def bet(self, amount):
        if amount <= 0:
            raise ValueError("Bet amount must be greater than zero")
        if amount > self.chips:
            raise ValueError("Not enough chips to place this bet")
        self.chips -= amount

    def win(self, amount):
        self.chips += amount

    def lose(self, amount):
        self.chips -= amount

    def is_broke(self):
        return self.chips <= 0

# Example usage:
if __name__ == "__main__":
    bet_manager = money()
    print("Starting chips:", bet_manager.get_chips())  # Starting with 500 chips

    bet_amount = 100
    print("Placing a bet of", bet_amount)
    bet_manager.bet(bet_amount)
    print("Remaining chips after bet:", bet_manager.get_chips())

    win_amount = 200
    print("Winning", win_amount)
    bet_manager.win(win_amount)
    print("Chips after winning:", bet_manager.get_chips())

    lose_amount = 300
    print("Losing", lose_amount)
    bet_manager.lose(lose_amount)
    print("Chips after losing:", bet_manager.get_chips())

    print("Is broke?", bet_manager.is_broke())
