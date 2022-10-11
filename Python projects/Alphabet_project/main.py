import pandas
file=pandas.read_csv("nato_phonetic_alphabet.csv")
Words_dict={word.letter:word.code for (letter,word) in file.iterrows()}

name=input("Enter the word: ")
res=True
while res:
    try:
        code_list=[Words_dict[letter.upper()] for letter in name]
        res=False
    except KeyError:
        print('sorry! only alphabets are allowed')
        name = input("Enter the word: ")
print(code_list)
