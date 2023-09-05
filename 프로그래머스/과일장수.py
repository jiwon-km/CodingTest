# https://school.programmers.co.kr/learn/courses/30/lessons/135808
# 무슨 기준으로 추천문제가 뽑히는지 모르겠다
# 1310-1323

def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    for i in range(0, len(score)//m):
        i *= m
        answer += min(score[i:i+m]) * m
    # for i in range(0, len(score) - m + 1, m):
    #     answer += min(score[i:i+m]) * m
    return answer
