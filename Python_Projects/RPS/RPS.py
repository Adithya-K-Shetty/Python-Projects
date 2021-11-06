import random
print(''' Welcome to rock paper scissor game
 press 1 for rock, 2 for paper, 3 for scissor ''')
print('\n')
user_input = int(input(" Input : "))

if user_input == 1:
    print("Your Move")
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
    computer_input = random.randint(1,6)
    print(computer_input)
    if computer_input == 1 or computer_input == 6:
        print("Comp Move")
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
        print("Its's A Draw!!")
    elif computer_input == 2 or computer_input == 5:
        print("Comp Move")
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("You Loose")
    elif computer_input == 3 or computer_input == 4:
        print("Comp Move")
        print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
        print("You win")
elif user_input == 2:
    print("Your Move")
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    computer_input = random.randint(1,6)
    if computer_input == 1 or computer_input == 6:
        print("Comp Move")
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
        print("You Win")
    elif computer_input == 2 or computer_input == 5:
        print("Comp Move")
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("It's A Draw!!")
    elif computer_input == 3 or computer_input == 4:
        print("Comp Move")
        print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
        print("You Lose")
elif user_input == 3:
    print("Your Move")
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
    computer_input = random.randint(1,6)
    if computer_input == 1 or computer_input == 6:
        print("Comp Move")
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
        print("You Lose")
    elif computer_input == 2 or computer_input == 5:
        print("Comp Move")
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("You Win")
    elif computer_input == 3 or computer_input == 4:
        print("Comp Move")
        print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
        print("It's A Draw!!")
else:
    print("Enter A Valid Input")
    
        
        
