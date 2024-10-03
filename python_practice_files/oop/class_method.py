class Student:
    def __init__(self, name, house, patronus=None):
        if not name:
            raise ValueError("Name is required")
        if house not in ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]:
            raise ValueError("House is not valid")
        if patronus and patronus not in ["Stag", "Otter", "Phoenix", "Badger", "Lion", "Eagle", "Snake", "Dog", "Hare", "Horse", "Wolf", "Doe", "Jack Russell Terrier"]:
            raise ValueError("Patronus is not valid")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
            return f"{self.name} from {self.house} with patronus {self.patronus}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"


def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: " )
    patronus = input("Patronus: ") or None
    return Student(name, house, patronus)
    

if __name__ == "__main__":
    main()