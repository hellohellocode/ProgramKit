#!/usr/bin/env python3

#BoBoBo#

close_check_print = False

def check_print(info):
    global close_check_print
    if not close_check_print:
        print(info)

def deal_input_line_cycle(func):
    while True:
        try:
            it = input()
            if 'stopit' == it:
                break
            func(it)
        except BaseException as e:
            print(e)

def deal_input_all(func, stop_input_flag):
    lines = []
    while True:
        it = input()
        if stop_input_flag == it:
            break
        lines.append(it)
    func(lines)
