from question_model import Question
from data import question_data
from  quiz_brain import QuizBrain



question_bank=[]
for question in question_data:
    question_text=question["question"]
    question_answer=question["correct_answer"]
    q1=Question(question_text,question_answer)
    question_bank.append(q1)

q2=QuizBrain(question_bank)
while q2.still_has_question():

    q2.next_question()
    if q2.still_has_question()==False:
         print("you have completed the quiz")
         print(f"your final score is: {q2.score}/{q2.question_no}")

