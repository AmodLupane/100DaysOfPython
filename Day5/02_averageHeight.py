student_height = input("Input list of student heights seperated by space\n").split()

for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])

sum = 0
number_of_students = 0

for height in student_height:
    sum += height
    number_of_students += 1

average_height = round(sum/number_of_students)
print(average_height)