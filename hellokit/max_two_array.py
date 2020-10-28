#!/usr/bin/env python3

#BoBoBo#

ipt_line1 = input()
ipt_line2 = input()

A = list(map(lambda s:abs(int(s)), ipt_line1.split(' ')))
B = list(map(int, ipt_line2.split(' ')))

A_max = max(A)
B_max = max(B)

print(A_max**2 + B_max**3)
