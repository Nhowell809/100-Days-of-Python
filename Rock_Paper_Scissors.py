import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("Let's get ready to rumble!")
user = input(f"What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")

RPS = [rock, paper, scissors]

user = int(user)

if user == 0:
  print(f"You selected: {RPS[0]}")
elif user == 1:
  print(f"You selected: {RPS[1]}")
else:
  print(f"You selected: {RPS[2]}")

computer = random.randint(0,2)
if computer == 0:
  print(f"The computer selected: {RPS[0]}")
elif computer == 1:
  print(f"The computer selected: {RPS[1]}")
else:
  print(f"The computer selected: {RPS[2]}")


if (user == 0 and computer == 0) or (user == 1 and computer == 1) or (user == 2 and computer == 2):
  print("It is a draw")
elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
  print("You win!")
else:
  print("The computer won. Try again!")
