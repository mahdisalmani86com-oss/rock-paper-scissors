import random
from pathlib import Path

# Name of the file used to store game statistics
DATABASE_FILE = Path(__file__).with_name("database.txt")


def load_scores():
    # Load previous scores from the database file
    scores = {"wins": 0, "losses": 0, "draws": 0}

    if DATABASE_FILE.exists():
        with open(DATABASE_FILE, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if "=" in line:
                    key, value = line.split("=", 1)
                    if key in scores:
                        try:
                            scores[key] = int(value)
                        except ValueError:
                            pass

    return scores


def save_scores(scores):
    # Save the current scores to the database file
    with open(DATABASE_FILE, "w", encoding="utf-8") as file:
        file.write(f"wins={scores['wins']}\n")
        file.write(f"losses={scores['losses']}\n")
        file.write(f"draws={scores['draws']}\n")


def decide_winner(player, computer):
    # Determine the winner of the round
    if player == computer:
        return "draw"

    if (
        (player == "Rock" and computer == "Scissors")
        or (player == "Paper" and computer == "Rock")
        or (player == "Scissors" and computer == "Paper")
    ):
        return "win"

    return "loss"


def main():
    choices = ["Rock", "Paper", "Scissors"]
    scores = load_scores()

    print("=== Rock, Paper, Scissors ===")
    print("Enter 0 to exit the game.")

    while True:
        print("\n1) Rock")
        print("2) Paper")
        print("3) Scissors")

        user_input = input("Your choice: ").strip()

        if user_input == "0":
            break

        options = {
            "1": "Rock",
            "2": "Paper",
            "3": "Scissors"
        }

        if user_input not in options:
            print("Invalid choice! Please enter 1, 2, 3, or 0.")
            continue

        player = options[user_input]
        computer = random.choice(choices)

        print(f"Your choice: {player}")
        print(f"Computer's choice: {computer}")

        result = decide_winner(player, computer)

        if result == "win":
            print("Congratulations! You won this round.")
            scores["wins"] += 1

        elif result == "loss":
            print("The computer won this round.")
            scores["losses"] += 1

        else:
            print("This round is a draw.")
            scores["draws"] += 1

        save_scores(scores)

        print(
            f"Total scores: Wins {scores['wins']} | "
            f"Losses {scores['losses']} | Draws {scores['draws']}"
        )

    save_scores(scores)

    print("\nGame over! Your scores have been saved.")
    print(
        f"Final results: Wins {scores['wins']}, "
        f"Losses {scores['losses']}, Draws {scores['draws']}"
    )


if __name__ == "__main__":
    main()
