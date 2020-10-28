#!/usr/bin/env python3

#BoBoBo#

close_check_print = False

def check_print(info):
    global close_check_print
    if not close_check_print:
        print(info)

def deal_input_line_cycle(func):
    global stop_input_cycle
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

def answer(total, customers):
    que = customers
    idx = 0

    running = {'idx_o': 0, 'idx_e': 0, 'que':customers}

    def get_2_odd():
        idx = running['idx_o']
        que = running['que']
        out = [] 
        for c in range(2):
            while(idx < len(que)):
                if int(que[idx]) % 2:
                    out.append(que[idx])
                    idx+=1
                    break
                idx+=1
        running['idx_o'] = idx
        return out

    def get_even():
        idx = running['idx_e']
        que = running['que']
        while(idx < len(que)):
            if int(que[idx]) % 2 == 0:
                running['idx_e'] = idx
                out = que[idx]
                idx+=1
                running['idx_e'] = idx
                return out
            else:
                idx+=1
        running['idx_e'] = idx
        return None

    p = 0
    asr = []
    while p < total:
        odds2 = get_2_odd()
        for po in range(len(odds2)):
            check_print(odds2[po] + ' ')
            asr.append(odds2[po])
            p+=1
        even = get_even()
        if None is even:
            continue
        asr.append(even)
        check_print(even + ' ')
        p+=1

    outstr = ' '.join(asr)
    print(outstr)

if __name__ == '__main__':
    def answer_line(line):
        params = line.split(' ')
        total = params[0]
        del params[0]
        answer(int(total), params)

    deal_input_line_cycle(answer_line)
