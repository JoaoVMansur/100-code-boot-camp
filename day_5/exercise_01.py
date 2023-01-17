student_heights = input("Input a list of student heights ").split()


total_student_heights = 0
for heights in student_heights:
    total_student_heights += int(heights)
n_students = 0
for n in student_heights:
    n_students += 1 

averge = round(total_student_heights / n_students)

print(averge)
