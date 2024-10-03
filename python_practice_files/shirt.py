import sys
import os
from PIL import Image, ImageOps

def main():
    # Check if exactly two command-line arguments are provided
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py <input_image> <output_image>")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input and output file extensions are valid
    extensions = (".png", "jpeg", ".jpg")

    if not (input_file.lower().endswith(extensions) and output_file.lower().endswith(extensions)):
        sys.exit("Invalid extensions for input and output files")

    # Check if the input and output file extensions match
    if os.path.splitext(input_file)[1].lower() != os.path.splitext(output_file)[1].lower():
        sys.exit("Input and output files must have the same valid extension")

    # Check if the input file exists
    if not os.path.exists(input_file):
        sys.exit(f"Input file '{input_file}' does not exist!")


    # Open the input image
    try:
        input_image = Image.open(input_file)

        # Open the shirt image
        shirt_image = Image.open("shirt.png")

        # Resize and crop the input image to match the size of the shirt image
        input_image = ImageOps.fit(input_image, shirt_image.size)

        # Overlay the shirt image on the input image
        input_image.paste(input_image, (0,0), shirt_image)

        # Save the result
        input_image.save(output_file)

    except Exception as e:
        sys.exit(f"Error: '{e}")

if __name__ == "__main__":
    main()