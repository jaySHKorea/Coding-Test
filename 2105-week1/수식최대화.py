'''
    구현
'''
import re
import itertools
from copy import deepcopy

def solution(expression):
    answer = 0
    exp_all = []

    operands = list(map(int,re.findall("[0-9]+",expression)))
    sign = list(re.findall("[*+-]",expression))

    for e in sign:
        if len(exp_all) == 3:
            break
        if e not in exp_all:
            exp_all.append(e)
    
    case = itertools.permutations(exp_all,len(exp_all))

    for c in case:
        exp = deepcopy(sign)
        operand = deepcopy(operands)
        for expr in c:
            i = 0
            while i < len(exp):
                if exp[i] == expr:
                    exp.pop(i)
                    a = operand.pop(i)
                    b = operand.pop(i)
                    if expr == '*':
                        operand.insert(i,a*b)
                    elif expr == '+':
                        operand.insert(i,a+b)
                    elif expr == '-':
                        operand.insert(i,a-b)
                else:
                    i += 1
        answer = max(answer,abs(operand[0]))        

    return answer

print(solution("100-200*300-500+20"))