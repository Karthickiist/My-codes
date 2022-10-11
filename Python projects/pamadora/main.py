import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=1
check_count=1
timer_loop=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps,check_count
    reps=1
    check_count=1
    windows.after_cancel(timer_loop)
    timer_label.config(text='TIMER')
    check.config(text="✔")
    canvas.itemconfig(timer_text,text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global check_count

    if reps%2==0:
        timer_label.config(text='BREAK',fg=RED)
        count=SHORT_BREAK_MIN*60
        if reps == 8:
            count = LONG_BREAK_MIN * 60
            reps = 0
            check_count=1
        reps += 1
    else:
        check.config(text="✔"*check_count)
        timer_label.config(text='WORK',fg=GREEN)
        count=WORK_MIN*60
        check_count+=1
        reps+=1
    count_down(count)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer_loop
    min=round(count/60)
    sec=round(count%60)
    if sec<10:
        sec=f"0{sec}"
    canvas.itemconfig(timer_text,text=f"{min}:{sec}")
    if count>0:
        timer_loop=windows.after(1000,count_down,count-1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
windows=tkinter.Tk()
windows.title("Karthick's Pamadora App")
windows.config(bg=YELLOW, padx=100, pady=50)

canvas=tkinter.Canvas(width=200, height=235)
image_file=tkinter.PhotoImage(file="tomato.png")
canvas.create_image(102,122,image=image_file)
canvas.configure(bg=YELLOW, highlightbackground = YELLOW)
timer_text=canvas.create_text(102,135,text="0",font=('calibri',35, "italic"))
canvas.grid(row=1, column=1)

timer_label=tkinter.Label(text='TIMER')
timer_label.config(fg=RED, bg=YELLOW, font=('calibri', 40, 'bold'))
timer_label.grid(row=0, column=1)

check=tkinter.Label(text="✔")
check.config(fg=RED, bg=YELLOW, font=('calibri',20,'bold'))
check.grid(row=2, column=1)

start_button=tkinter.Button(text='START',command=start_timer)
start_button.grid(row=2, column=0)

reset_button=tkinter.Button(text='RESET', command=reset_timer)
reset_button.grid(row=2, column=2)







windows.mainloop()