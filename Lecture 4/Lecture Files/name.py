import sys


if len(sys.argv) < 2:
    sys.exit("hello, I forgot my name")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)
