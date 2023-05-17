#!/usr/bin/python3

def noc_c(my_string):
    output = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            output += char
        return output
