from random import randint

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


def user_side():
    if ask_user == 0:
        return rock
    elif ask_user == 1:
        return paper
    else:
        return scissors


def computer_side():
    if computer_ans == 0:
        return rock
    elif computer_ans == 1:
        return paper
    else:
        return scissors

def result():
    if ask_user == 0 and computer_ans == 2:
        return "You won"
    elif ask_user == 1 and computer_ans == 0:
        return "you won"
    elif ask_user == 2 and computer_ans == 1:
        return "You won"
    elif ask_user == computer_ans:
        return "its a draw"
    else:
        return "You lose"

for game in range(11):
    ask_user=int(input("What do you choose? Type 0 for rock ,1 for paper, 2 for scissors :\n"))
    print(user_side())
    print("Computer chose:")
    computer_ans=randint(0,2)
    print(computer_side())
    print((result()))
