
def main_letter():
    with open("root_letter.txt") as f:
        return f.read()


f=open("names.txt",'r')
res=True
letter_dictionary={}
while res:
    name=f.readline().strip()
    if name!="":
        letter_text=main_letter()
        new_letter_text=letter_text.replace("name",name)
        letter_dictionary[name]=new_letter_text

    else:
        res=False

for i in letter_dictionary:
    with open(f"./output_letters/letter_for_{i}",'w') as f:
        f.write(letter_dictionary[i])

