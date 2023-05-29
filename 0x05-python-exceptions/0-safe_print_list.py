#!/usr/bin/python3
def safe_print_list(my_list=[], x =0):
    var = 0
    try:
        for i in my_list[:x]:
            print("{}".format(i), end="")
            var += 1
        print()
        return var
    except IndexError:
        print()
        return var
