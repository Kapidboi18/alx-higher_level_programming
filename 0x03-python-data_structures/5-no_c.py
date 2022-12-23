#!/usr/bin/python3

def no_c(my_string):
    remove_c_C = ''
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            remove_c_C += ch
    return (remove_c_C)
