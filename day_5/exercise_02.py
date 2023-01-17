scores = input("input a list of students scores:")
list_scores = scores.split(" ")

nota_alta = 0

for score in list_scores:
    if int(score) > nota_alta:
        nota_alta = int(score)
print(f"The highest score in the class is: {nota_alta}")