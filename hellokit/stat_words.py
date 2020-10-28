#!/usr/bin/env python3

#BoBoBo#

import re

close_check_print = False

def check_print(info):
    global close_check_print
    if not close_check_print:
        print(info)

def deal_input_all(func, stop_input_flag):
    lines = []
    while True:
        it = input()
        if stop_input_flag == it:
            break
        lines.append(it)
    return func(lines)

def find(lines):
    w = lines[0]
    check_print(w)
    del lines[0]
    r = r'\b' + w + r'\b'
    pattern = re.compile(r)
    check_print(lines)
    l = list(map(lambda s:len(pattern.findall(s)), lines))
    check_print(l)
    return sum(l)

print(deal_input_all(find, "-1"))
