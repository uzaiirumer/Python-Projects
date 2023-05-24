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
game_images = [rock, paper, scissors]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor \n"))
if user_input >= 3 or user_input < 0:
    print("You type invalid number. You loose!")
else:
    print(game_images[user_input])

    computer_choice = random.randint(0,2)

    print("computer Choose:")
    print(game_images[computer_choice])


    if user_input == 0 and computer_choice == 2:
        print("You Win!")
    elif user_input == 2 and computer_choice == 0:
        print("You loose!")
    elif computer_choice > user_input:
        print("You Loose")
    elif computer_choice == user_input:
        print("Its Draw")
    elif user_input > computer_choice:
        print ("You Win")
