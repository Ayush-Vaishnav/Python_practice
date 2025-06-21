#adv rock paper

import random

emoji = {
    "rock": "🪨",
    "paper": "📄",
    "scissor": "✂️"
}

player_score = 0
computer_score = 0

while True:
    print("\nChoose rock, paper or scissor")
    a = input("You: ").lower()

    items = ["rock", "paper", "scissor"]
    bot = random.choice(items)

    if a not in items:
        print("❌ Invalid input! Try again.")
        continue

    print(f"You chose {emoji[a]}  |  Computer chose {emoji[bot]}")

    if a == bot:
        print("🤝 It's a tie!")
    elif (a == "rock" and bot == "scissor") or \
         (a == "scissor" and bot == "paper") or \
         (a == "paper" and bot == "rock"):
        print("✅ You win this round!")
        player_score += 1
    else:
        print("💻 Computer wins this round!")
        computer_score += 1

    # Show score
    print(f"Score → You: {player_score} | Computer: {computer_score}")

    # Ask to play again
    again = input("\nPlay again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing!")
        break
