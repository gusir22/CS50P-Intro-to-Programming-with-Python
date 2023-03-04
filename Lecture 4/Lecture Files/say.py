import cowsay
import sys

from sayings import hello  # Custom library


if len(sys.argv) == 2:
    cowsay.milk(hello(sys.argv[1]))


