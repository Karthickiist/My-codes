class quizz_brain:
    def __init__(self, list):
        self.q_no=0
        self.q_list = list
        self.score=0

    def still_has_question(self):
        if self.q_no<len(self.q_list):
            return True
        else:
            return False

    def next_question(self):
        question=self.q_list[self.q_no]
        self.q_no+=1
        answer=input(f"Q {self.q_no}:{question.text} (True/False): ").lower()
        if self.check_answer(answer,question.answer.lower()):
            print('Your answer is correct..')
            self.score+=1

        else:
            print('wrong answer')
        print(f"Your score is: {self.score}/{self.q_no}")
        print(f"The correct answer was {question.answer}")
        print("\n")


    def check_answer(self,my_ans,crct_ans):
        return my_ans==crct_ans



