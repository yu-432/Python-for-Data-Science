from sys import argv

if len(argv) == 1:
    exit()
if len(argv) > 2:
    assert len(argv) == 2, "more than one argument is provided"
    exit()

try:
    num = int(argv[1])
except ValueError:
    raise AssertionError("argument is not an integer")

if num % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
