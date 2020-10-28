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

def answer(lines):
    ns = {}
    sn = {}

    def bind(s, n):
        if s[0] == 'U':
            print('unknown command')
            return
        try:
            b = ns[n]
            print(s + ' bind failed')
        except KeyError:
            try:
                cs = sn[s]
                print(s + ' bind fail')
            except KeyError:
                ns[n] = s
                sn[s] = n
                print(s + ' bind success')
                
    def scan(s, n):
        try:
            b = ns[n]
            print(s + ' pay to ' + b)
        except KeyError:
            print(s + ' scan fail')

    def unbind(s, n):
        if s[0] == 'U':
            print('unknown command')
            return
        try:
            b = ns[n]
            if b == s:
                del ns[n]
                print(s + ' unbind success')
            else:
                print(s + ' unbind fail')
        except KeyError:
                print(s + ' unbind fail')

    def ev(line):
        #ls = line.split(' ')
        ls = re.split(r'\s+', line)
        if ls[1] == 'bind':
            bind(ls[0], ls[2])
        elif ls[1] == 'scan':
            scan(ls[0], ls[2])
        elif ls[1] == 'unbind':
            unbind(ls[0], ls[2])
        else:
            print('unknown command')

    for l in lines:
        ev(l)
        check_print(ns)

deal_input_all(answer, "-1")
