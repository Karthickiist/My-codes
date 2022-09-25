import random
def logo():
    guess='''
       ____     _   _ U _____ u ____    ____          __  __  U _____ u 
U /"___|uU |"|u| |\| ___"|// __"| u/ __"| u     U|' \/ '|u\| ___"|/ 
\| |  _ / \| |\| | |  _|" <\___ \/<\___ \/      \| |\/| |/ |  _|"   
 | |_| |   | |_| | | |___  u___) | u___) |       | |  | |  | |___   
  \____|  <<\___/  |_____| |____/>>|____/>>      |_|  |_|  |_____|  
  _)(|_  (__) )(   <<   >>  )(  (__))(  (__)    <<,-,,-.   <<   >>  
 (__)__)     (__) (__) (__)(__)    (__)          (./  \.) (__) (__) 
    '''
    print(guess)

logo()
print("Hello...Welcome to the number guessing game...")
number=random.randint(1,100)
print("I have selected a number between 1 and 100, now guess what the number is...")
level=input("Select your level (Easy/Hard): ")
if level=="hard":
    attempt=5
else:
    attempt=10
print(f"you have {attempt} chances to guess the number...")
while attempt>0:
    num=int(input("Take a guess: "))
    if num>number:
        print("oh! It is higher..")
    elif num<number:
        print("sorry! it is lower")
    elif num==number:
        print("You guessed te number correctly")
        print(f"you have {attempt} guesses left")
        print("Congratulations! you win")
        input()
        exit()
    attempt-=1
    print(f"you have {attempt} guesses left")
    print("Try again")

print("Sorry! you run out of chances...You lose")
print("Better luck next time..")
input()