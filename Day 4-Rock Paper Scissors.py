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

import random

user_choice = int(input("Choose between rock, paper, or scissors. Enter 0 for rock, 1 for paper, and 2 for scissors: "))
computer_choice = random.randint(0, 2)

if user_choice == 0:
    print(f"You chose {user_choice}\n{rock}")
    if computer_choice == 1:
        print(f"Computer chose\n{paper}\nYou lose")
    elif computer_choice == 2:
        print(f"Computer chose\n{scissors}\nYou win")
    elif computer_choice == 0:
        print(f"Computer chose\n{rock}\nIt's a draw")
elif user_choice == 1:
    print(f"You chose {user_choice}\n{paper}")
    if computer_choice == 0:
        print(f"Computer chose\n{rock}\nYou win")
    elif computer_choice == 2:
        print(f"Computer chose\n{scissors}\nYou lose")
    elif computer_choice == 1:
        print(f"Computer chose\n{paper}\nIt's a draw")
elif user_choice == 2:
    print(f"You chose {user_choice}\n{scissors}")
    if computer_choice == 0:
        print(f"Computer chose\n{rock}\nYou lose")
    elif computer_choice == 1:
        print(f"Computer chose\n{paper}\nYou win")
    elif computer_choice == 2:
        print(f"Computer chose\n{scissors}\nIt's a draw")
else:
    print("Invalid choice. Please enter 0, 1, or 2.")
