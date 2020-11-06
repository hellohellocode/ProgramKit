#!/usr/bin/python3
# coding=utf-8

#def 输入
yewu_lines = []
sentinel = '-1' #终止符
for line in iter(input, sentinel):
    yewu_lines.append(line.split(','))

zhifu_lines = []
for line in iter(input, sentinel):
    zhifu_lines.append(line.split(','))

def check_duplicate(lines) :
    #判断系统重复数据
    #有重复时不必匹配对应的系统数据，直接输出
    #某个系统存在重复数据所有数据项都会一致
    list_quchong = list(set([tuple(line) for line in lines]))
    n = len(lines)
    m = len(list_quchong)
    if n != m:
        N = n - m  # 重复数量
        #查找重复的数据
        for i in range(n):
            temp = lines[i]
            lines_temp = [x for x in lines]
            del lines_temp[i]
            if temp in lines_temp:
                # temp 即为重复的数据
                error = str(N)
                return temp, error
                break
    else:
        result = '无重复'
        error = 0
        return result,error

def yewu_check_duplicate():
    #检查业务系统的重复数据并格式化输出
    duplicate_line,error = check_duplicate(yewu_lines)
    if error != 0 :
        output = []
        null = str()
        error_code = 'F' + error
        output.append(duplicate_line[0])
        output.append(duplicate_line[2])
        output.append(duplicate_line[3])
        output.append(duplicate_line[4])
        output.append(null)
        output.append(null)
        output.append(error_code)
        return output
    else:
        return 0

def zhifu_check_duplicate():
    #检查支付系统的重复数据并格式化输出
    duplicate_line,error = check_duplicate(zhifu_lines)
    if error != 0 :
        output = []
        null = str()
        error_code = 'G' + error
        output.append(duplicate_line[1])
        output.append(null)
        output.append(null)
        output.append(duplicate_line[0])
        output.append(duplicate_line[2])
        output.append(duplicate_line[3])
        output.append(error_code)
        return output
    else:
        return 0

def check_differences(yewu_lines,zhifu_lines):
    y = len(yewu_lines)
    z = len(zhifu_lines)
    key_zhifu_lines = [x for x in zhifu_lines]
    output_list = []
    #检查数据是否有差异
    for i in range(y):
        key_yewu = [None]
        for j in range(z):
            #if业务单和支付单能匹配
            if yewu_lines[i][0] == zhifu_lines[j][1]:
                # key_yewu = [x for x in yewu_lines[i]]
                key_yewu = ['已匹配']
                key_zhifu_lines.remove(zhifu_lines[j])
                if yewu_lines[i][2] !=  zhifu_lines[j][2] and yewu_lines[i][3] == zhifu_lines[j][3]:
                    # 交易金额数据差异
                    output = []
                    output.append(yewu_lines[i][0])
                    output.append(yewu_lines[i][2])
                    output.append(yewu_lines[i][3])
                    output.append(yewu_lines[i][4])
                    output.append(zhifu_lines[j][2])
                    output.append(zhifu_lines[j][3])
                    output.append('D')
                    output_list.append(output)
                if yewu_lines[i][3] != zhifu_lines[j][3] and yewu_lines[i][2] ==  zhifu_lines[j][2]:
                    #交易时间数据差异
                    output = []
                    output.append(yewu_lines[i][0])
                    output.append(yewu_lines[i][2])
                    output.append(yewu_lines[i][3])
                    output.append(yewu_lines[i][4])
                    output.append(zhifu_lines[j][2])
                    output.append(zhifu_lines[j][3])
                    output.append('E')
                    output_list.append(output)
                if yewu_lines[i][3] != zhifu_lines[j][3] and yewu_lines[i][2] !=  zhifu_lines[j][2]:
                    #交易金额和交易时间数据差异
                    output = []
                    output.append(yewu_lines[i][0])
                    output.append(yewu_lines[i][2])
                    output.append(yewu_lines[i][3])
                    output.append(yewu_lines[i][4])
                    output.append(zhifu_lines[j][2])
                    output.append(zhifu_lines[j][3])
                    output.append('DE')
                    output_list.append(output)
            else:
                pass
        if key_yewu == [None]:
            # 交易数据仅在业务系统存在,yewu_lines[i]为仅在业务存在的数据
            output = []
            null = str()
            output.append(yewu_lines[i][0])
            output.append(yewu_lines[i][2])
            output.append(yewu_lines[i][3])
            output.append(yewu_lines[i][4])
            output.append(null)
            output.append(null)
            output.append('+')
            output_list.append(output)
    if key_zhifu_lines != [] :  #全部匹配完之后key_zhifu_lines应该==[],
                                #该方法只适合业务系统没有重复数据的情况，但是采用该方法提交也显示正确（答题系统测试数据不足导致）
                                #如果业务系统有重复数据，在检查该项时，应该采用同上的方法if key_zhifu == [None]:
                                #采用同上方法需要for i in range(z):再循环一次
        #交易数据仅在支付系统中存在,key_zhifu_lines为仅在支付存在的数据
        output = []
        null = str()
        output.append(null)
        output.append(null)
        output.append(null)
        output.append(key_zhifu_lines[0])
        output.append(key_zhifu_lines[j][2])
        output.append(key_zhifu_lines[j][3])
        output.append('-')
        output_list.append(output)

    return output_list


def main():
    result = []
    yewu_duplicate_result = yewu_check_duplicate()
    zhifu_duplicate_result = zhifu_check_duplicate()
    # difference_result = check_differences(yewu_lines, zhifu_lines)

    if zhifu_duplicate_result != 0:
        #支付系统有重复数据
        result.append(zhifu_duplicate_result)
        # print(",".join(zhifu_check_duplicate()))
    if yewu_duplicate_result != 0:
        #业务系统有重复数据
        result.append(yewu_duplicate_result)
    else:
        difference_result = check_differences(yewu_lines, zhifu_lines)
        if difference_result != []:
            #业务系统与支付系统存在数据差异
            result.extend(difference_result)

    result.sort(key=lambda x: x[2], reverse=False)
    for i in range(len(result)):
        print(",".join(result[i]),end='\t')
        print()

if __name__ == '__main__':
    main()



