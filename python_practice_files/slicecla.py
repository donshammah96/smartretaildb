import sys

# slice is a command that allows us to take a list and tell the compiler where we want the compiler to consider the start of the list and the end of the list
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)
