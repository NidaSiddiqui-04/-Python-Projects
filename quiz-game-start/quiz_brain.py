class QuizBrain:

    def __init__(self,question_list):
        self.question_no=0
        self.question_list=question_list
        self.score=0




    def next_question(self,):
        current_ques=self.question_list[self.question_no]
        self.question_no+=1
        user_answer=input(f"Q.{self. question_no} :{current_ques.text} (True/False): ")
        self.check_answer(user_answer,current_ques.answer)
    def still_has_question(self):
        return self.question_no<len(self.question_list)


    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            print("You got it")
            print(f"the correct answer is:{correct_answer}")
            self.score += 1
            print(f"Your score is :{self.score}/{self.question_no}")
        else:
            print("you are wrong")
            print(f"the correct answer is:{correct_answer}")

            print(f"Your score is :{self.score}/{self.question_no}")



        print("\n")


