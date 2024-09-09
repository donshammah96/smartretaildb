students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.strip().split(",")
        student = {"name": name, "house": house}
        students.append(student)
for student in students:
    print(f"{student['name']} is in house {student['house']}")