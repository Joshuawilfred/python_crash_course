#!/usr/bin/python3
j = 1
while j < 100:
    if j % 10 == 0:
        j = int(j + (j/10) + 1)
        continue
    print("{:02d}".format(j), end=", " if j < 89 else "\n")
    j += 1
