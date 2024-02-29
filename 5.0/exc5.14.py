students_names = input("Type a list of the students names separated by a space: ")
students_grades = input("Type a list of the students grades separated by a space: ")

students_names_split = students_names.split()
students_grades_split = [float(grade) for grade in students_grades.split()]

if len(students_names_split) != len(students_grades_split):
    print("Both lists have to be the same lenth.")
else:
    students_grades_dicreasing_order = sorted(zip(students_names_split, students_grades_split), key=lambda x: x[1], reverse=True)
    print("Grade's list in decreasing order:")
    for student, grade in students_grades_dicreasing_order:
        print(f"{student}: {grade}")