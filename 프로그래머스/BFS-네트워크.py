# https://school.programmers.co.kr/learn/courses/30/lessons/43162
from collections import deque

def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def solution(n, computers):
    graph = [[] for _ in range(n)] # 그래프 초기화
    visited = [False] * n
    count = 0

    # 인접행렬 -> 연결리스트 변환
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
                
    for i in range(n):
        if not visited[i]:
            bfs(graph, i, visited)
            count += 1

    return count

# 시간 복잡도 : O(n^2), 인접 행렬을 인접 리스트로 변환하는 과정
# 그러나 굳이 필요없는 과정이기에 수정하여 풀어보자