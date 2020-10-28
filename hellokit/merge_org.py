#!/usr/bin/env python3

#BoBoBo#

import re

close_check_print = True

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

def merge_lines(lines):
    num = lines[0]
    del lines[0]

    merge_it = lines[-1].split(' ')
    mo = merge_it[0]
    to = merge_it[1]
    del lines[-1]

    lines = list(map(lambda s : s.split(' '), lines))
    check_print(lines)
    
    morg = list(filter(lambda l : True if l[0] == mo else False, lines))[0]
    check_print(morg)
    torg = list(filter(lambda l : True if l[0] == to else False, lines))[0]
    check_print(torg)

    mo_name = morg[3]
    to_name = torg[3]

    def ev_org_line(ss):
        check_print(ss)
        if ss[0] == mo:
            ss[4] = "1"
        if ss[2] == mo:
            ss[2] = to
            ss[3] = re.sub(mo_name, to_name, ss[3])
        check_print("dealed line:" + str(ss))
        return ss

    lines = list(map(ev_org_line, lines))
    return lines

lines = deal_input_all(merge_lines, "-1")
for l in lines:
    print(" ".join(l))
