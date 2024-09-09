import sys
import random
from pyfiglet import Figlet

# Get the list of available fonts
fonts = Figlet().getFonts()

if len(sys.argv) == 1:
    # No font specified, choose a random font
    font = random.choice(fonts)
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    # Font specified by the user
    if sys.argv[2] in fonts:
        font = sys.argv[2]
    else:
        print("Error: Invalid font")
        sys.exit(1)
else:
    print("Usage: figlet.py [-f | --font FONTNAME]")
    sys.exit(1)

# Prompt the user for input
user_input = input("Input: ")

# Render the text using pyfiglet
figlet = Figlet(font=font)
output_text = figlet.renderText(user_input)

# Output the rendered text
print("Output:\n" + output_text)
