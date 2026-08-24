"""A small terminal game: Rock, Paper, Scissors."""

import random


CHOICES = ("rock", "paper", "scissors")
WINS_AGAINST = {
	"rock": "scissors",
	"paper": "rock",
	"scissors": "paper",
}


def get_choice():
	"""Ask until the player enters a valid move or quits."""
	while True:
		answer = input("Choose rock, paper, scissors (or q to quit): ").strip().lower()
		if answer in CHOICES:
			return answer
		if answer in ("q", "quit"):
			return None
		print("Please type rock, paper, scissors, or q.")


def play_round(player_choice):
	computer_choice = random.choice(CHOICES)
	print(f"Computer chose: {computer_choice}")

	if player_choice == computer_choice:
		return "tie"
	if WINS_AGAINST[player_choice] == computer_choice:
		return "win"
	return "loss"


def main():
	player_score = 0
	computer_score = 0
	ties = 0

	print("\n=== Rock, Paper, Scissors ===")
	print("First player to 5 points wins.\n")

	while player_score < 5 and computer_score < 5:
		player_choice = get_choice()
		if player_choice is None:
			print("\nThanks for playing!")
			return

		result = play_round(player_choice)
		if result == "win":
			player_score += 1
			print("You win this round!")
		elif result == "loss":
			computer_score += 1
			print("Computer wins this round.")
		else:
			ties += 1
			print("This round is a tie.")

		print(f"Score: You {player_score} - Computer {computer_score} | Ties: {ties}\n")

	if player_score == 5:
		print("You won the match! Nice work.")
	else:
		print("The computer won the match. Try again!")


if __name__ == "__main__":
	main()