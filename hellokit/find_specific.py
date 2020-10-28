#!/usr/bin/env python3

#BoBoBo#

poet = {}
for i in range(4):
    poet[i] = input()

nums = input()

r = list(map(lambda t:poet[t[0]][int(t[1])-1], zip(range(4), nums)))
print("".join(r))
