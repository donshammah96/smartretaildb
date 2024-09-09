#Gets rid of get_name and get_house functions
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.strip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

#RPasses a lambda (anon) function to the key parameter of the sorted function
for student in sorted(students, key= lambda student: student["name"]):
    print(f"{student['name']} is in house {student['house']}")