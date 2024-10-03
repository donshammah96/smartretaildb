class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Name is required")
        if house not in ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]:
            raise ValueError("House is not valid")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
            return f"{self.name} from {self.house} with patronus {self.patronus}"


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: " )
    patronus = input("Patronus: ")
    return Student(name, house, patronus)
    

if __name__ == "__main__":
    main()