import tkinter as tk
import random

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def play_game(player_choice):
    computer_choice = get_computer_choice()

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.config(text=f"Player chose: {player_choice}\nComputer chose: {computer_choice}\n{result}")

root = tk.Tk()
root.title("Rock Paper Scissors Game")

choices = ["Rock", "Paper", "Scissors"]
for idx, choice in enumerate(choices):
    button = tk.Button(root, text=choice, command=lambda c=choice: play_game(c))
    button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()