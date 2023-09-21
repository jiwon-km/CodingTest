# https://school.programmers.co.kr/learn/courses/30/lessons/12978

def solution(N, roads, K):
    answer = 0
    cost = [[217000000 for _ in range(N)] for _ in range(N)]
    
    for a, b, c in roads:
        cost[a-1][b-1] = min(cost[a-1][b-1], c)
        cost[b-1][a-1] = min(cost[b-1][a-1], c)
       
    for k in range(N):
        cost[k][k] = 0
        for i in range(N):
            for j in range(N):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

    answer = 0
    for cst in cost[0]:
        if cst<=K:
            answer += 1
            
    return answer
