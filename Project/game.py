import random

game = input("enter a game you want to play(gn/rps): ")

if game == "gn":
    guess = random.randint(1, 10)
    while True:
        number = int(input("Select  a number: ").lower().strip())
        if number == guess:
            print("You got it!")
            break
        elif number > guess:
            print("Your guess is too high.")
        elif number < guess:
            print("Your guess is too low.")


elif game == "rps":


    VALID_MOVES = ["rock", "paper", "scissors"]

    # What beats what: key beats value
    BEATS = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }



    def get_player_move():
        """Keep asking until the player types a valid move."""
        while True:
            move = input("Enter your move (rock/paper/scissors, or 'q' to quit): ").lower().strip()
            if move == "q":
                return None
            if move in VALID_MOVES:
                return move
            print(f"'{move}' isn't valid. Please choose rock, paper, or scissors.")


    def get_computer_move():
        return random.choice(VALID_MOVES)


    def decide_round(player, computer):
        """Return 'player', 'computer', or 'draw'."""
        if player == computer:
            return "draw"
        if BEATS[player] == computer:
            return "player"
        return "computer"


    def play_game(rounds=5):
        count_p1 = 0
        count_p2 = 0
        count_draw = 0

        round_num = 1
        while round_num <= rounds:
            print(f"\n--- Round {round_num} ---")
            player1 = get_player_move()
            if player1 is None:
                print("Game ended early.")
                break

            player2 = get_computer_move()
            print(f"Computer chose: {player2}")

            result = decide_round(player1, player2)
            if result == "draw":
                print("It's a draw!")
                count_draw += 1
            elif result == "player":
                print("You win this round!")
                count_p1 += 1
            else:
                print("Computer wins this round!")
                count_p2 += 1

            print(f"Score -> You: {count_p1} | Computer: {count_p2} | Draws: {count_draw}")
            round_num += 1

        print("\n=== Final Results ===")
        print(f"You: {count_p1} | Computer: {count_p2} | Draws: {count_draw}")
        if count_p1 > count_p2:
            print("🎉 You win the match!")
        elif count_p2 > count_p1:
            print("💻 Computer wins the match!")
        else:
            print("🤝 The match is a tie!")


    def main():
        print("=== Rock, Paper, Scissors ===")
        while True:
            try:
                rounds = int(input("How many rounds do you want to play? "))
                if rounds > 0:
                    break
                print("Please enter a positive number.")
            except ValueError:
                print("Please enter a valid number.")

        play_game(rounds)

        while True:
            again = input("\nPlay again? (y/n): ").lower().strip()
            if again == "y":
                print()
                main()
                break
            elif again == "n":
                print("Thanks f gor playing!")
                break
            else:
                print("Please answer y or n.")




    if __name__ == "__main__":
        main()
