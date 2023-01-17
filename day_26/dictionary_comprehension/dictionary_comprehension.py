import random
import pandas
#Dictionary comprehension with a list
names = ["Alex", "John", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_score = {student: random.randint(1, 100)   for student in names}
print(students_score)


#Dictionary comprehension with dictionary
passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
print(passed_students)


#Looping through a data frame
student_dic = {
 "student": ["Angela", "James", "Lily"],
 "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dic)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":

        print(row.score)