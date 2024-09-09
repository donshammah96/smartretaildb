name = input("What is your name? ")

#Closes the file automatically after the block of code
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
