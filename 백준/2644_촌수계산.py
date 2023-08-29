# https://www.acmicpc.net/problem/2644

import sys
from collections import deque

read = sys.stdin.readline
n = int(read())
p1, p2 = map(int, read().split())
m = int(read())
e_list = [list(map(int, read().split())) for _ in range(m)]
graph = [[] for _ in range(n + 1)]

# e_list 2 graph
for e in e_list:
  graph[e[0]].append(e[1])
  graph[e[1]].append(e[0])

visited = [0] * (n + 1)

def bfs(v, target_v):
  global visited, graph
  queue = deque()
  queue.append(v)
  visited[v] = 1

  while queue:
    nv = queue.popleft()
    if nv == target_v:
      return visited[nv] - 1
    for e in graph[nv]:
      if visited[e] == 0:
        queue.append(e)
        visited[e] = visited[nv] + 1

  return -1


print(bfs(p1, p2))
