# https://school.programmers.co.kr/learn/courses/30/lessons/17682

import re

def solution(dartResult):
    answer = 0
    flag = 0
    power_dict = {'S' : 1, 'T' : 3, 'D' : 2}
    
    result = re.findall(r'(\d+[SDT][*#]?)', dartResult)
    
    for i in range(2, -1, -1):
        num = int(re.findall(r'(\d+)', result[i])[0])
        power = re.findall(r'[SDT]', result[i])[0]
        prize = re.findall(r'[*#]', result[i])
        ans = int(num) ** power_dict[power]
        
        if flag:
            ans *= 2
            flag -= 1
            
        if prize:
            if prize[0] == '*':
                ans *= 2
                flag += 1
            elif prize[0] == '#':
                ans *= -1
        
        answer += ans
    return answer
