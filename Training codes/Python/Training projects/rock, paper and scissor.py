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

choice=[rock, paper, scissors]
my_choice=int(input("Enter your choice (0 for rock, 1 for paper and 2 for scissors): "))
print("\nYou chose:")
if my_choice>2 or my_choice<0:
  print("Invalid entry")
  exit()
print(choice[my_choice])
com_choice=random.randint(0,2)
print("\nComputer chose: ")
print(choice[com_choice])
if my_choice==com_choice:
    print("It's a draw shot.. Try again")
elif my_choice==0 and com_choice==2:
    print("You win")
elif my_choice==0 and com_choice==1:
    print("You lose")
elif my_choice==1 and com_choice==0:
    print("You win")
elif my_choice==1 and com_choice==2:
    print("You lose")
elif my_choice==2 and com_choice==0:
    print("You lose")
elif my_choice==2 and com_choice==1:
    print("You win")

