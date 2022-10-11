from tkinter import *
import time
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizzInterface:
    def __init__(self, quizbrain : QuizBrain):
        self.score=0
        self.quiz=quizbrain
        self.window=Tk()
        self.window.title("Karthick's Quizz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_text=Label(text="SCORE:0")
        self.score_text.config(padx=20, pady=20, bg=THEME_COLOR, fg='white')
        self.score_text.grid(row=0, column=1)

        self.canvas=Canvas(height=250, width=300)
        self.quest=self.canvas.create_text(150,125,width=280, text="Question Text", font=('arial',20,'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2)

        true_image=PhotoImage(file="./images/true.png")
        false_image=PhotoImage(file="./images/false.png")
        self.right_button=Button(image=true_image, command=self.true_press)
        self.right_button.config(padx=20, pady=20)
        self.right_button.grid(row=2, column=0)

        self.false_button=Button(image=false_image, command=self.false_pressed)
        self.false_button.config(padx=20, pady=20)
        self.false_button.grid(row=2, column=1)
        self.question_change()

        self.window.mainloop()

    def question_change(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text=self.quiz.next_question()
            self.score_text.config(text=f"SCORE:{self.quiz.score}")
            self.canvas.itemconfig(self.quest, text=q_text)
        else:
            self.score_text.config(text=f"SCORE:{self.quiz.score}")
            self.canvas.itemconfig(self.quest, text=f"End of the Quiz\n Your score is: {self.quiz.score}/{self.quiz.question_number}")
            self.right_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)

    def true_press(self):
        self.feedback(self.quiz.check_answer('True'))

    def false_pressed(self):
        self.feedback(self.quiz.check_answer('False'))

    def feedback(self,response):
        if response:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.question_change)


