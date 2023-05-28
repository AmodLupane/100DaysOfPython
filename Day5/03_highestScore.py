student_scores = input("Enter scores of students seperated by space: \n").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

max_score = student_scores[0]

for n in range(1, len(student_scores)):
    if max_score < student_scores[n]:
        max_score = student_scores[n]

print(f"The highest score is: {max_score}")