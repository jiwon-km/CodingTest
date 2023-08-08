# https://school.programmers.co.kr/learn/courses/30/lessons/49993#fn1

def solution(skills, skill_trees):
    skill_order = []
    answer = 0
    skill_order = [s for s in skills]

    for skill in skill_trees:
        ans = [s for s in skill if s in skill_order]
        if ans == skill_order[:len(ans)]:
            answer += 1
        
    return answer
