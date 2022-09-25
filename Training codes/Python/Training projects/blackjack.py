import os
import random


def logos():
    logo="""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
    print(logo)

cards=[11,1,2,3,4,5,6,7,8,9,10,10,10,10]



def mytotal():
    if len(my_cards)==2 and sum(my_cards)==21:
        return 0
    if 11 in my_cards and sum(my_cards)>21:
        my_cards.remove(11)
        my_cards.append(1)
    return sum(my_cards)


def comtotal():
    if len(com_cards)==2 and sum(com_cards)==21:
        return 0
    if 11 in com_cards and sum(com_cards)>21:
        com_cards.remove(11)
        com_cards.append(1)
    return sum(com_cards)


def final_result(myscore,comscore):
    if myscore==comscore:
        print("This is a draw match...")
    elif myscore==0:
        print("Super! you won the game..")
    elif comscore==0:
        print("You lose. computer won the game")
    elif myscore>21 and comscore<21:
        print("You lose. computer won the game")
    elif comscore>21 and myscore<21:
        print("Super! you won the game..")
    elif myscore>comscore:
        print("Super! you won the game..")
    else:
        print("You lose. computer won the game")


def start():
    for i in range(2):
        my_cards.append(random.choice(cards))
        com_cards.append(random.choice(cards))
    res = True
    while res:
        print(f"Your cards: {my_cards}, and your total is {mytotal()}")
        print(f"Computer's first card: {com_cards[0]}")
        if mytotal() == 0 or comtotal() == 0 or mytotal() > 21 or comtotal() > 21:
            res = False
        else:
            my_choice = input("Get/pass: ").lower()
            if not my_choice == 'get':
                res = False
            else:
                my_cards.append(random.choice(cards))
            com_choice = random.choice(['get', 'pass'])
            if not com_choice == 'get':
                if comtotal()<17:
                    com_cards.append(random.choice(cards))
                res = False
            else:
                com_cards.append(random.choice(cards))

    print(f"You final cards: {my_cards}, Total: {mytotal()}")
    print(f"Computer's final cards: {com_cards}, Total: {comtotal()}")
    final_result(mytotal(), comtotal())
    input("Press Enter")


while True:
    os.system('cls')
    my_cards = []
    com_cards = []
    logos()
    start_opt=input("Do you want to start the game (y/n)?: ").lower()
    if start_opt=='y':
        start()
    else:
        input("Press Enter")
        exit()
