# 수식 최대화
# https://school.programmers.co.kr/learn/courses/30/lessons/67257

# 스택 다루는 법이 미숙해서 레퍼런스 참고하였음 -> 추후 재풀이 예정

import re
from itertools import permutations


def calc_operator(operator_stack, value_stack):
        operator = operator_stack.pop()
        right = value_stack.pop()
        left = value_stack.pop()
        if operator == '+':
            value_stack.append(left + right)
        elif operator == '-':
            value_stack.append(left - right)
        elif operator == '*':
            value_stack.append(left * right)

def solution(expression):
    answer = []
    pattern = r"(\d+|[-+*/])"
    tokens = re.findall(pattern, expression)
    operator = ''

    for token in tokens:
        if len(operator) == 3: break
        try: int(token)
        except: 
            if token not in operator:
                 operator += token

    order_candidate = list(permutations(operator))
    
    for order in order_candidate:
        operator_stack = []
        value_stack = []
        i = 0
        while i < len(expression):
            if expression[i] == ' ':
                i += 1
                continue
            if expression[i] in '0123456789':
                j = i
                while j < len(expression) and expression[j] in '0123456789':
                    j += 1
                value_stack.append(int(expression[i:j]))
                i = j
            elif expression[i] in '+-*':
                while (operator_stack and operator_stack[-1] in '+-*' and
                       order.index(operator_stack[-1]) >= order.index(expression[i])):
                    calc_operator(operator_stack, value_stack)
                operator_stack.append(expression[i])
                i += 1


        while operator_stack:
            calc_operator(operator_stack, value_stack)

        answer.append(abs(value_stack[0]))

    return max(answer)
