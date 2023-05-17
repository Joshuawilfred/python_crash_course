#!/usr/bin/python3

def search_replace(my_list, serch, replace):
    ret = []
    for item in my_list:
        if item == search:
            ret.append(replace)
        else:
            ret.append(item)
     return ret
