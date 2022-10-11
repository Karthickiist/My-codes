from tkinter import *

windows=Tk()
windows.title("Miles to KM Converter")
windows.grid()
windows.config(padx=20,pady=20)

label=Label(text='Miles')
label.grid(row=0, column=2)
label_1=Label(text='is equal to')
label_1.grid(row=1, column=0)
label_2=Label(text='KM')
label_2.grid(row=1,column=2)
label_3=Label(text='0')
label_3.grid(row=1,column=1)

miles_input=Entry()
miles_input.grid(row=0,column=1)

def calculation():
    miles=miles_input.get()
    kilo_meter=(int(miles)*1.609)
    km=round(kilo_meter,2)
    label_3['text']=km

button=Button(text='Calculate', command=calculation)
button.grid(row=2,column=1)



windows.mainloop()