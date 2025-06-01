#Grading Program
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades={}
for grades in student_scores:

    if student_scores[grades]>=91 and student_scores[grades]<=100:
        student_scores[grades]="Outstanding"
    elif student_scores[grades]>=81 and student_scores[grades]<=90:
        student_scores[grades]="Exceeds Expectations"
    elif student_scores[grades]>=71 and student_scores[grades]<=80:
        student_scores[grades]="Acceptable"
    else:
        student_scores[grades]="Fail"
student_grades.update(student_scores)
print(student_grades)