number_students = int(input("Insert the number of students:  "))

students_grades = {}  

for _ in range(number_students):
    name = input("Insert the student's name: ")
    grade = float(input(f"Insert {name}'s grade: "))
    students_grades[name] = grade


approved_students = {name: grade for name, grade in students_grades.items() if grade >= 7}

print("Original dictionary:", students_grades)
print("Approved students:", approved_students)