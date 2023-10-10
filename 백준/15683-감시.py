# https://www.acmicpc.net/problem/15683
# 감시
# 리팩토링을 해도 엉망이다

import sys
import itertools
import copy

def get_input():
    n, m = map(int, sys.stdin.readline().split())
    map_info = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    return n, m, map_info

def find_cctvs(n, m, map_info):
    cctvs = []
    positions = []
    for i in range(n):
        for j in range(m):
            if 1 <= map_info[i][j] <= 5:
                cctvs.append(map_info[i][j])
                positions.append((i, j))
    return cctvs, positions
  
def turn_cctv(x, y, d, cctv_type, map_info):
  dir1_list = {0: [[1, 0]], 1: [[-1, 0]], 2: [[0, 1]], 3: [[0, -1]]}
  dir2_list = {0: [[0, 1], [0, -1]], 1: [[1, 0], [-1, 0]]}
  dir3_list = {
      0: [[0, 1], [-1, 0]],
      1: [[-1, 0], [0, -1]],
      2: [[0, -1], [1, 0]],
      3: [[1, 0], [0, 1]]
  }
  dir4_list = {
      0: [[0, 1], [-1, 0], [0, -1]],
      1: [[0, 1], [-1, 0], [1, 0]],
      2: [[0, 1], [0, -1], [1, 0]],
      3: [[-1, 0], [0, -1], [1, 0]]
  }
  dir5_list = {0: [[0, 1], [-1, 0], [0, -1], [1, 0]]}

  cctvs = [dir1_list, dir2_list, dir3_list, dir4_list, dir5_list]
  dir_list = cctvs[cctv_type]

  m = len(map_info[0])
  n = len(map_info)
  for dir in dir_list[d]:
    nx, ny = x, y
    while True:
      nx = nx + dir[0]
      ny = ny + dir[1]
      if nx < 0 or nx >= n or ny < 0 or ny >= m or map_info[nx][ny] == 6:
        break
      if map_info[nx][ny] != 0:
        continue
      map_info[nx][ny] = '#'
  return map_info

def count_zeros(map_info):
  return sum(row.count(0) for row in map_info)

n, m, map_info = get_input()
cctvs, pos_cctv = find_cctvs(n, m, map_info)

dir_counts = {1: [0, 1, 2, 3], 2: [0, 1], 3: [0, 1, 2, 3], 4: [0, 1, 2, 3], 5: [0]}

candidate = list(itertools.product(*(dir_counts[c] for c in cctvs)))

ans = []

for cand in candidate:
    new_map = copy.deepcopy(map_info)
    for i, (x, y) in enumerate(pos_cctv):
        new_map = turn_cctv(x, y, cand[i], cctvs[i] - 1, new_map)
    ans.append(count_zeros(new_map))

print(min(ans))

# n, m = map(int, sys.stdin.readline().split())
# map_info = []
# for _ in range(n):
#   map_info.append(list(map(int, sys.stdin.readline().split())))

# cctv_list = [[] for _ in range(5)]
# cctvs = []
# for i in range(n):
#   for j in range(m):
#     for k in range(1, 6):
#       if map_info[i][j] == k:
#         cctv_list[k - 1].append([i, j])
#         cctvs.append(k)
# cctvs.sort()


# counts = {1: [0, 1, 2, 3], 2: [0, 1], 3: [0, 1, 2, 3], 4: [0, 1, 2, 3], 5: [0]}

# temp = []
# for c in cctvs:
#   temp.append(counts[c])
# candidate = list(itertools.product(*temp))

# pos_cctv = []
# for i, cctv in enumerate(cctv_list):
#   for c in cctv:
#     pos_cctv.append(c)

# ans = []

# for cand in candidate:
#   new_map = copy.deepcopy(map_info)
#   for i, cctv in enumerate(pos_cctv):
#     new_map = turn_cctv(cctv[0], cctv[1], cand[i], cctvs[i] - 1, new_map)

#   count = 0
#   for row in new_map:
#     for item in row:
#       if item == 0:
#         count += 1
#   ans.append(count)

# print(min(ans))
