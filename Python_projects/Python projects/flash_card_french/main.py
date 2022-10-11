from tkinter import *
import pandas
import random
flip_click=NONE
random_num=0


def word_operation():
    global flip_click, random_num
    windows.after_cancel(flip_click)
    random_num=random.randint(0, len(data_dict)-1)
    random_french=data_dict[random_num]['French']
    english_answer=data_dict[random_num]['English']
    canvas.itemconfig(bg_image, image=bg_image_load)
    canvas.itemconfig(language_txt,text='FRENCH', fill='black')
    canvas.itemconfig(word_txt, text=random_french, fill='black')
    def flip_card():
        canvas.itemconfig(bg_image, image=bg_image_back)
        canvas.itemconfig(language_txt, text='ENGLISH', fill='white')
        canvas.itemconfig(word_txt, text=english_answer, fill='white')
    flip_click=windows.after(3000,flip_card)

def known_click():
    data_dict.remove(data_dict[random_num])
    word_operation()

def stop_application():
    learn_data=pandas.DataFrame(data_dict)
    learn_data.to_csv('./data/learn_data.csv')
    exit()


#data load
try:
    data=pandas.read_csv("./data/learn_data.csv.csv")
    data_dict=data.to_dict(orient='record')
except FileNotFoundError:
    data=pandas.read_csv("./data/french_words.csv")
    data_dict=data.to_dict(orient='record')


windows=Tk()
windows.title("Karthick's Flip card ")
windows.config(padx=50, pady=50)

canvas=Canvas(height=526, width=800)
bg_image_load=PhotoImage(file='./images/card_front.png')
bg_image_back=PhotoImage(file='./images/card_back.png')
bg_image=canvas.create_image(400,263,image=bg_image_load)
word_txt=canvas.create_text(400,263, text="WORD", font=('ariel', 60, 'bold'))
language_txt=canvas.create_text(400,150, font=('ariel', 40, 'italic'), text="WORD")
canvas.grid(row=0, column=0, columnspan=2)

#buttons
right_img=PhotoImage(file='./images/right.png')
wring_img=PhotoImage(file='./images/wrong.png')
right_button=Button(image=right_img, command=known_click)
right_button.grid(row=1, column=0)

wrong_button=Button(image=wring_img, command=word_operation)
wrong_button.grid(row=1, column=1)

stop_button=Button(text='STOP FLIP', command=stop_application)
stop_button.grid(row=2,columnspan=2, column=0)

word_operation()


windows.mainloop()