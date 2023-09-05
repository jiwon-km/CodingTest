# https://school.programmers.co.kr/learn/courses/30/lessons/120871

def solution(n):
    answer = []
    i = 1
    while len(answer) < n:
        if i % 3 and '3' not in str(i):
            answer.append(i)
        i += 1
    
    return answer[-1]
