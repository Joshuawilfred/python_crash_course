#!/usr/bin/python3
import random
number = random.randoint(-10000, 10000)
mes = f"null"
last = number % 10 if number > 0 else number % -10
if last != 0:
    mes = f"and is greater that 5" if last > 5 \
            else f"and is less than 6 and not 0"
        else:
            mes = "and is 0"
            /* YOur good to go */
            print(f"Last digit of {number:d} is {last:d} {mes}")
