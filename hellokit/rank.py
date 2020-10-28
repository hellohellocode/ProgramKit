#!/usr/bin/env python3

#BoBoBo#

def rank(num, scores, find):
    r = num
    for i in range(num):
        if scores[i] <= find:
            r-=1

    print(r + 1)


while True:
    num = input()
    if '-1' == num:
        break
    scores = input().split(' ')
    scores = list(map(lambda s : int(s), scores))
    find = input()
    rank(int(num), scores, int(find))
