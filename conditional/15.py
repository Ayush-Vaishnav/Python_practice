# # Rock, Paper, Scissors: Take input from two players and decide the winner based on standard game rule

# while True:

#     a= input("Enter rock,paper or scissor: ").lower()

#     import random
#     items = ["rock", "paper", "scissor"]
#     bot = random.choice(items)

#     if a==bot:
#         print("Its a tie!")

#     elif a== "scissor" and bot == "paper":
#         print("You win!")

#     elif a=="rock" and bot == "scissor":
#         print("You win!")

#     elif a=="paper" and bot =="scissor":
#         print("You lose!, it was a scissor")

#     elif a=="paper" and bot =="rock":
#         print("You win!")

#     elif a== "scissor" and bot == "rock":
#         print("You lose!, it was a rock")

#     elif a=="rock" and bot == "paper":
#         print("You lose!, it was a paper")

#     else:
#         print("Invalid")


import random

while True:
    a = input("Enter rock, paper or scissor: ").lower()
    items = ["rock", "paper", "scissor"]
    bot = random.choice(items)

    print(f"Computer chose: {bot}")

    if a not in items:
        print("Invalid input! Please choose rock, paper, or scissor.")
    elif a == bot:
        print("It's a tie!")
    elif (a == "rock" and bot == "scissor") or \
         (a == "scissor" and bot == "paper") or \
         (a == "paper" and bot == "rock"):
        print("You win!")
    else:
        print("You lose!")

    print()  # Just a space between rounds

    