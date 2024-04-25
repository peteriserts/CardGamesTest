from blackjack import BlackjackGame
from poker import PokerGame

def display_menu():
    print("Welcome to the Casino!")
    print("1. Play Blackjack")
    print("2. Play Poker")
    print("3. Quit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            num_players = int(input("Enter number of players for Blackjack: "))
            blackjack_game = BlackjackGame(num_players)
            blackjack_game.play_game()
        elif choice == '2':
            num_players = int(input("Enter number of players for Poker: "))
            poker_game = PokerGame(num_players)
            poker_game.play_game()
        elif choice == '3':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
