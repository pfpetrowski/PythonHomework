
user_selection = input("Please select rock, paper, or scissors.")
print("You selected", user_selection+".")

possible_selections = ["rock", "paper", "scissors"]
import random
number = random.randint(0,2)
computer_choice=possible_selections[number]
print("The computer chooses ", computer_choice+".")

while computer_choice == user_selection:
	print("It is a tie.")
	user_selection = input("Please select rock, paper, or scissors.")
	print("You selected", user_selection+".")
	possible_selections = ["rock", "paper", "scissors"]
	import random
	number = random.randint(0,2)
	computer_choice=possible_selections[number]
	print("The computer chooses ", computer_choice+".")
if computer_choice == "rock" and user_selection == "paper":
	print("You Win!")
elif computer_choice == "rock" and user_selection == "scissors":
	print("You loose. Better luck next time!")
elif computer_choice == "scissors" and user_selection == "rock":
	print("You Win!")
elif computer_choice == "scissors" and user_selection == "paper":
	print("You loose. Better luck next time!")
elif computer_choice == "paper" and user_selection == "rock":
	print("You loose. Better luck next time!")
elif computer_choice == "paper" and user_selection == "scissors":
	print("You Win!")
else:
	print("Error: Please try again.")
