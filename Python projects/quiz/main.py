from data import question_data
from question_model import questions
from quiz_brain import quizz_brain

question_bank=[]
for i in question_data:
    question_bank.append(questions(i['question'],i['correct_answer']))

quizz=quizz_brain(question_bank)
while quizz.still_has_question():
    quizz.next_question()

print("You have successfully completed the quizz")
print(f"Your final score is: {quizz.score}/{quizz.q_no}")