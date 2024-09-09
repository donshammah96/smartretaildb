import os
import sys
import csv

def main():

    if len(sys.argv) != 3:
        sys.exit("Error: Incorrect number of commandline arguments!")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(input_file):
        sys.exit(f"The file '{input_filename}' does not exist!")

    try:
        with open("before.csv", "r") as input_file:
            reader = csv.DictReader(input_file)
            fieldnames = ["first", "last", "house"]
            rows = []

            for row in reader:
                first, last = row["name"].split(",")
                house = row["house"]
                rows.append({"first": first, "last": last, "house": house})
    except Exception as e:
        sys.exit(f"Could not read file '{input_file}'")

    try:
        with open("after.csv", "w", newline="") as output_file:
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    except Exception as e:
        sys.exit(f"Could not write to the output file '{output_file}' ")


if __name__ == "__main__":
    main()