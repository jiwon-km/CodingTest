# https://softeer.ai/practice/info.do?idx=1&eid=395

import sys

read = sys.stdin.readline

n, m = map(int, read().split())
item_list = [list(map(int, read().split())) for _ in range(m)]
ans = 0

# sol. 단가순으로 정렬 -> 차곡차곡 채우기
item_list.sort(key=lambda x : x[1], reverse=True)

def solution():
  global n, m, item_list, ans
  for item in item_list:
    if n <= item[0]:
      ans += n * item[1]
      return ans
    else:
      ans += item[0] * item[1]
      n -= item[0]
        
print(solution())
