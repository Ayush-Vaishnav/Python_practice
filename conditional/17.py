#gui version rock ppr

import tkinter as tk
import random
  
# Score variables
player_score = 0
computer_score = 0

# Game logic
def play(player_choice):
    global player_score, computer_score

    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)

    result = ""
    if player_choice == computer_choice:
        result = "🤝 It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissor") or \
         (player_choice == "scissor" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        result = "✅ You win!"
        player_score += 1
    else:
        result = "💻 Computer wins!"
        computer_score += 1

    result_label.config(text=result)
    player_choice_label.config(text=f"You: {player_choice.capitalize()} 🧍")
    computer_choice_label.config(text=f"Computer: {computer_choice.capitalize()} 💻")
    score_label.config(text=f"Score → You: {player_score} | Computer: {computer_score}")

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors 🪨📄✂️")
root.geometry("400x300")

# Labels
player_choice_label = tk.Label(root, text="You: ", font=("Arial", 12))
player_choice_label.pack()

computer_choice_label = tk.Label(root, text="Computer: ", font=("Arial", 12))
computer_choice_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score → You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="🪨 Rock", width=10, command=lambda: play("rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="📄 Paper", width=10, command=lambda: play("paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissor_btn = tk.Button(button_frame, text="✂️ Scissor", width=10, command=lambda: play("scissor"))
scissor_btn.grid(row=0, column=2, padx=5)

# Run the GUI
root.mainloop()
