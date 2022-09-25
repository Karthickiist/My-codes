import random
import os
def stages():
    stages = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''']
    return stages
def logo():
    logo = ''' 
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/    '''
    print(logo)
def wordlist():
    word_list = [
        'abruptly',
        'absurd',
        'abyss',
        'affix',
        'askew',
        'avenue',
        'awkward',
        'axiom',
        'azure',
        'bagpipes',
        'bandwagon',
        'banjo',
        'bayou',
        'beekeeper',
        'bikini',
        'blitz',
        'blizzard',
        'boggle',
        'bookworm',
        'boxcar',
        'boxful',
        'buckaroo',
        'buffalo',
        'buffoon',
        'buxom',
        'buzzard',
        'buzzing',
        'buzzwords',
        'caliph',
        'cobweb',
        'cockiness',
        'croquet',
        'crypt',
        'curacao',
        'cycle',
        'daiquiri',
        'dirndl',
        'disavow',
        'dizzying',
        'duplex',
        'dwarves',
        'embezzle',
        'equip',
        'espionage',
        'euouae',
        'exodus',
        'faking',
        'fishhook',
        'fixable',
        'fjord',
        'flapjack',
        'flopping',
        'fluffiness',
        'flyby',
        'foxglove',
        'frazzled',
        'frizzled',
        'fuchsia',
        'funny',
        'gabby',
        'galaxy',
        'galvanize',
        'gazebo',
        'giaour',
        'gizmo',
        'glowworm',
        'glyph',
        'gnarly',
        'gnostic',
        'gossip',
        'grogginess',
        'haiku',
        'haphazard',
        'hyphen',
        'iatrogenic',
        'icebox',
        'injury',
        'ivory',
        'ivy',
        'jackpot',
        'jaundice',
        'jawbreaker',
        'jaywalk',
        'jazziest',
        'jazzy',
        'jelly',
        'jigsaw',
        'jinx',
        'jiujitsu',
        'jockey',
        'jogging',
        'joking',
        'jovial',
        'joyful',
        'juicy',
        'jukebox',
        'jumbo',
        'kayak',
        'kazoo',
        'keyhole',
        'khaki',
        'kilobyte',
        'kiosk',
        'kitsch',
        'kiwifruit',
        'klutz',
        'knapsack',
        'larynx',
        'lengths',
        'lucky',
        'luxury',
        'lymph',
        'marquis',
        'matrix',
        'megahertz',
        'microwave',
        'mnemonic',
        'mystify',
        'naphtha',
        'nightclub',
        'nowadays',
        'numbskull',
        'nymph',
        'onyx',
        'ovary',
        'oxidize',
        'oxygen',
        'pajama',
        'peekaboo',
        'phlegm',
        'pixel',
        'pizazz',
        'pneumonia',
        'polka',
        'pshaw',
        'psyche',
        'puppy',
        'puzzling',
        'quartz',
        'queue',
        'quips',
        'quixotic',
        'quiz',
        'quizzes',
        'quorum',
        'razzmatazz',
        'rhubarb',
        'rhythm',
        'rickshaw',
        'schnapps',
        'scratch',
        'shiv',
        'snazzy',
        'sphinx',
        'spritz',
        'squawk',
        'staff',
        'strength',
        'strengths',
        'stretch',
        'stronghold',
        'stymied',
        'subway',
        'swivel',
        'syndrome',
        'thriftless',
        'thumbscrew',
        'topaz',
        'transcript',
        'transgress',
        'transplant',
        'triphthong',
        'twelfth',
        'twelfths',
        'unknown',
        'unworthy',
        'unzip',
        'uptown',
        'vaporize',
        'vixen',
        'vodka',
        'voodoo',
        'vortex',
        'voyeurism',
        'walkway',
        'waltz',
        'wave',
        'wavy',
        'waxy',
        'wellspring',
        'wheezy',
        'whiskey',
        'whizzing',
        'whomever',
        'wimpy',
        'witchcraft',
        'wizard',
        'woozy',
        'wristwatch',
        'wyvern',
        'xylophone',
        'yachtsman',
        'yippee',
        'yoked',
        'youthful',
        'yummy',
        'zephyr',
        'zigzag',
        'zigzagging',
        'zilch',
        'zipper',
        'zodiac',
        'zombie',
    ]
    return word_list
print(logo())
print("Guess the word...")
stages=stages()
word_list = wordlist()
word=random.choice(word_list)
word_length=len(word)
display=[]
for i in range(word_length):
    display.append('_')
life=6
while '_' in display and life>0:
    inlet = input("Enter a letter: ")
    os.system('cls')
    count = 0
    check=False
    if inlet in display:
        print(f"You have already guessed the letter {inlet}")
    for i in word:
        if inlet == i:
            display[count] = inlet
            check=True
        count+=1
    if check==False:
        life-=1
        print(f"The letter {inlet} not in the word...")
    print(''.join(display))
    print(stages[life])
if '_' not in display:
    print("you win the game...")
else:
    print("You lose,,.")

input()