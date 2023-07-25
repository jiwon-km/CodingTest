# https://school.programmers.co.kr/learn/courses/30/lessons/154540
# 무인도 여행
# 테스트 케이스만 생각하다가, maps[0][0]이 무조건 X일 것이라고 가정해 days 초기화를 잘못 해줘서 오류 발생했음
# maps가 필요없음 -> 이미 필터링 함

from collections import deque

def bfs(graph, x, y, visited):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    queue= deque()
    queue.append([x, y])
    visited[x][y] = True
    
    days = int(graph[x][y])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if not visited[nx][ny] and graph[nx][ny] != '0':
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                    days += int(graph[nx][ny])
    
    return days

def solution(maps):
    answer = []
    maps = [map.replace('X', '0') for map in maps]
    visited = [[False for x in range(len(maps[0]))] for x in range(len(maps))]
    
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if not visited[i][j] and maps[i][j] != '0':
                day = bfs(maps, i, j, visited)
                if day != 0:
                    answer.append(day)
    answer.sort()
    
    if not answer:
        return [-1]
    
    return answer
