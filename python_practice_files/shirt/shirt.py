import sys
import os
from PIL import Image, ImageOps

def main():
    # Check if exactly two command-line arguments are provided
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py <input_image> <output_image>")

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    # Check if the input and output file extensions are valid
    valid_extensions = ('.jpg', '.jpeg', '.png')
    
    if not (input_filename.lower().endswith(valid_extensions) and output_filename.lower().endswith(valid_extensions)):
        sys.exit("Error: The input and output files must have .jpg, .jpeg, or .png extensions")

    # Check if the input and output file extensions match
    if os.path.splitext(input_filename)[1].lower() != os.path.splitext(output_filename)[1].lower():
        sys.exit("Error: The input and output files must have the same extension")

    # Check if the input file exists
    if not os.path.exists(input_filename):
        sys.exit(f"Error: The file '{input_filename}' does not exist")

    try:
        # Open the input image
        input_image = Image.open(input_filename)

        # Open the shirt image
        shirt_image = Image.open("shirt.png")

        # Resize and crop the input image to match the size of the shirt image
        input_image = ImageOps.fit(input_image, shirt_image.size)

        # Overlay the shirt image on the input image
        input_image.paste(shirt_image, (0, 0), shirt_image)

        # Save the result
        input_image.save(output_filename)

    except Exception as e:
        sys.exit(f"Error: {e}")

if __name__ == "__main__":
    main()