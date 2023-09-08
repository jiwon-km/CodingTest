import sys

read = sys.stdin.readline

n = int(read())
m = int(read())
graph = [list(map(int, read().split())) for _ in range(m)]

def floyd_warshall(graph):
    distance = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
      distance[i][i] = 0
      
    for data in graph:
      a, b, c = data
      distance[a-1][b-1] = min(distance[a-1][b-1], c)
      # distance[data[0]-1][data[1]-1] = data[2]
      
    for k in range(n):
      for i in range(n):
        for j in range(n):
          if distance[i][k] != float('inf') and distance[k][j] != float('inf'):
            if distance[i][j] > distance[i][k] + distance[k][j]:
              distance[i][j] = distance[i][k] + distance[k][j]  

    for i in range(n):
      for j in range(n):
        if distance[i][j] == float('inf'):
          distance[i][j] = 0
  
    return distance


# print(floyd_warshall(graph))
result = floyd_warshall(graph)
for row in result:
    print(*row)
