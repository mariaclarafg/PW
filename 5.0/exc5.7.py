number_students = int(input("Insert the number of students: "))

student_grades = {}  

for _ in range(number_students):
    name = input("Insert the student's name: ")
    grade = float(input(f"Insert {name}'s grade: "))
    student_grades[name] = grade


students_rounded_grades = {name: round(grade) for name, grade in student_grades.items()}

print("Original dictionary:", student_grades)
print("Dictionary with the rounded grades:", students_rounded_grades)