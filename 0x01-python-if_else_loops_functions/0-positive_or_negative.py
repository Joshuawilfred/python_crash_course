#!/usr/bin/pythons3
import random
number = random.randint(-10, 10)


if number > 0:
    print(f"{numer:d} is positive")
elif number< 0:
    print(f"{number:d} is negative")
else:
    print(f"{number:d} is zero")
