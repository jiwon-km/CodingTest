# https://school.programmers.co.kr/learn/courses/30/lessons/49189
from collections import deque

def bfs(start, adj):
    n = len(adj)
    distance = [-1] * n 
    queue = deque([start])
    
    distance[start] = 0

    while queue:
        x = queue.popleft()
        for y in adj[x]:
            if distance[y] == -1:
                queue.append(y)
                distance[y] = distance[x] + 1
                
    return distance

def solution(n, edges):
    adj = [[] for _ in range(n)]
    for edge in edges:
        adj[edge[0]-1].append(edge[1]-1)
        adj[edge[1]-1].append(edge[0]-1)
    distance = bfs(0, adj)
    
    return distance.count(max(distance))
