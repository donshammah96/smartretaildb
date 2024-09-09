# Use csv library to read csv file
import csv

students = []

try:
    with open("students1.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                students.append({"name": row["name"], "home": row["home"]})
            except KeyError as e:
                print(f"Missing expected column in CSV: {e}")
except FileNotFoundError:
    print("The file students1.csv was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Passes a lambda (anon) function to the key parameter of the sorted function
try:
    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is from {student['home']}")
except Exception as e:
    print(f"An error occurred while sorting or printing: {e}")