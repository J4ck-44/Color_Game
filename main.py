import random
valid_colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink"]
def display_scoreboard(player_name, games_won, games_lost):
    print("\nScoreboard:")
    print(f"Name of the player: {player_name}")
    print(f"Number of games won: {games_won}")
    print(f"Number of games lost: {games_lost}")

def color_game():
    player_name = input("Please enter the name for the scoreboard: ")
    games_won = 0
    games_lost = 0

    while True:
        print("\n1> Start Game")
        print("2> Exit")
        choice = input("Please choose an option: ")

        if choice == '1':
            m_color = random.choice(valid_colors)
            attempts = 5
            a_left = attempts

            while a_left > 0:
                user_color = input("Please enter the color: ").strip().lower()

                if user_color not in valid_colors:
                    print("You have entered an invalid color.")
                    continue

                if user_color == m_color:
                    print("You won the game!")
                    print(f"Number of attempts: {attempts - a_left + 1}")
                    print(f"Total number of attempts: {attempts}")
                    games_won += 1
                    break
                else:
                    a_left -= 1
                    print(f"Your guess was wrong, please try again.")
                    print(f"Number of attempts left: {a_left}")

            if a_left == 0:
                print(f"You lost the game! The correct color was: {m_color}")
                games_lost += 1

            while True:
                print("\n1> See Scoreboard")
                print("2> Play Again")
                print("3> Exit")
                end_choice = input("Please choose an option: ")

                if end_choice == '1':
                    display_scoreboard(player_name, games_won, games_lost)
                    break
                elif end_choice == '2':
                    break
                elif end_choice == '3':
                    print("Thank you for playing!")
                    return
                else:
                    print("Invalid choice, please try again.")

        elif choice == '2':
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice, please try again.")

color_game()