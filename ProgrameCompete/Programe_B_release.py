#!/usr/bin/python3
# coding=utf-8
"""
    Author：ZhuMengru
    Version：1.0
    Date：28/10/2020
    Function：题目解答-计算幸存者人数
"""

def input_lists():
    '''
    获取输出，返回决斗轮数z 和 初始武力值initial_lists
    '''
    lines = input().split()
    z = int(lines[0])
    initial_lists = []
    initial_lists.append(lines)
    return z,initial_lists


def result_lists(initial_lists):
    '''
    :param initial_lists: 初始武力值列表集合
    :return: 一轮决斗后的武力值列表集合
    '''
    all_lists = []
    for l in range(len(initial_lists)):
        i = 1
        for i in range(i,len(initial_lists[l])-1):
            for j in range(i + 1, len(initial_lists[l])):
                list_temp = [x for x in initial_lists[l]]
                if(int(initial_lists[l][i]) != 0 and int(initial_lists[l][j]) != 0): #不与已死亡的进行决斗
                    if int(initial_lists[l][i]) > int(initial_lists[l][j]):
                        list_temp[i] = (int(initial_lists[l][i]) - int((initial_lists[l][j])))
                        list_temp[j] = 0
                    if int(initial_lists[l][i]) < int(initial_lists[l][j]):
                        list_temp[i] = 0
                        list_temp[j] = int(initial_lists[l][j]) - int((initial_lists[l][i]))
                    if int(initial_lists[l][i]) == int(initial_lists[l][j]):
                        list_temp[i] = list_temp[j] = 0
                    all_lists.append(list_temp)
            i += 1
    #删除重复
    result_lists = list(set([tuple(line) for line in all_lists]))
    return result_lists


def main():
    '''
    执行决斗
    :return: 最终决斗之后可能结果数量
    '''
    global input_lists
    z,input_lists = input_lists()

    for r in range(z):
        output_lists = result_lists(input_lists)
        input_lists = output_lists

    print(len(output_lists))


if __name__ == '__main__':
    main()

