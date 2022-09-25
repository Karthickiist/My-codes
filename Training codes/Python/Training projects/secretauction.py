import os
def logo():
    hammer = '''
                             ___________
                             \         /
                              )_______(
                              |"""""""|_.-._,.---------.,_.-._
                              |       | | |               | | ''-.
                              |       |_| |_             _| |_..-'
                              |_______| '-' `'---------'` '-'
                              )"""""""(
                             /_________\\
                           .-------------.
                          /_______________\\
    '''
    print(hammer)
logo()
res='yes'
auction={}
print('Welcome to the secret auction... Start bidding...')
while res=='yes':
    name=input("What is your name?: ")
    amount=int(input("How much you want to bid? $"))
    auction[name]=amount
    res=input("Are there any other bitters?(yes/no): ")
    os.system('cls')
winner=0
name=""
for i in auction:
    if auction[i]>winner:
        winner=auction[i]
        name=i

print(f"The winner is {name} with the bid of {winner}")
input()