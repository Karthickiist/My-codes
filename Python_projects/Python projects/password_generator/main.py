from tkinter import *
from tkinter.messagebox import *
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(3, 4)
    nr_numbers = random.randint(3, 4)
    password = ''
    for i in range(1, nr_letters + 1, 1):
        rnd = random.randint(0, len(letters) - 1)
        password += letters[rnd]
    for i in range(1, nr_numbers + 1, 1):
        rnd = random.randint(0, len(numbers) - 1)
        password += numbers[rnd]
    for i in range(1, nr_symbols + 1, 1):
        rnd = random.randint(0, len(symbols) - 1)
        password += symbols[rnd]
    password_generated = ''.join(random.sample(password, len(password)))
    password_box.insert(0,password_generated)
    pyperclip.copy(password_generated)

def search_details():
    website=website_box.get()
    try:
        with open('data.json', 'r') as f:
            loaded_data=json.load(f)
            print(loaded_data)
    except FileNotFoundError:
        showinfo("OOPS", 'Data file not found!')
    else:
        try:
            showinfo(f'{website}', f"Email: {loaded_data[website]['E-mail: ']}\n"
                                   f"Password: {loaded_data[website]['Password: ']}")
        except KeyError:
            showinfo("OOPS", 'Website not found!')
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_entry():
    website_txt = website_box.get()
    email_txt=email_box.get()
    password_txt=password_box.get()
    new_data={website_txt:
                  {'E-mail: ':email_txt,
                   'Password: ':password_txt}}

    confirmation=askyesno('Is details entered correct?', f'Details entered:-\nWebsite:{website_txt}\nE-mail:{email_txt}\n'
                                                         f'Password:{password_txt}')
    if confirmation:
        if len(website_txt)==0 or len(email_txt)==0 or len(password_txt)==0:
            showinfo('Empty field:-','Hey! you have left some field empty. Please check again..')
        else:
            try:
                with open('data.json','r') as f:
                    data=json.load(f)
                    data.update(new_data)
            except FileNotFoundError:
                with open('data.json','w') as f:
                    json.dump(new_data,f,indent=4)
            else:
                with open('data.json','w') as f:
                    json.dump(data,f,indent=4)

            website_box.delete(0,END)
            password_box.delete(0,END)
            showinfo("DATA SAVED",'Your data has been saved')


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Karthick's Passward Manager")
window.config(padx=50, pady=50)

canvas=Canvas(height=200, width=200)
logo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0, column=1)
#labels

website_label=Label(text='Website:')
website_label.grid(row=1, column=0)

email_label=Label(text='Email/Username:')
email_label.grid(row=2, column=0)

password_label=Label(text='Password:')
password_label.grid(row=3, column=0)

#box
website_box=Entry(width=24)
website_box.grid(row=1, column=1)
website_box.focus()


email_box=Entry(width=34)
email_box.insert(END,'karthick@gmail.com')
email_box.grid(row=2, column=1, columnspan=2)

password_box=Entry(width=24)
password_box.config()
password_box.grid(row=3, column=1)

#buttons

add_button=Button(text="ADD", command=add_entry)
add_button.grid(row=4, column=1, columnspan=2)

generate_button=Button(text='GENERATE', command=generate_password)
generate_button.grid(row=3, column=2)

search_button=Button(text='SEARCH', command=search_details)
search_button.grid(row=1, column=2)











window.mainloop()