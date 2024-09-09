students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.strip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]

#Returns a sorted list of students by name
for student in sorted(students, key=get_house, reverse=True):
    print(f"{student['name']} is in house {student['house']}")