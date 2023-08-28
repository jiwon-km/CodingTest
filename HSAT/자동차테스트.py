# https://softeer.ai/practice/info.do?idx=1&eid=1717

import sys
from bisect import bisect_left, bisect_right

read = sys.stdin.readline
n, q = map(int, read().split())
n_list = list(map(int, read().split()))
n_list.sort()
median_list = [int(read()) for _ in range(q)]

for median in median_list:
    # 예외 조건
    pos = bisect_left(n_list, median)
    if pos == n or n_list[pos] != median or median == n_list[0] or median == n_list[-1]:
        print('0')
    # 가짓수 계산
    else:
        low_num = pos
        high_num = n - bisect_right(n_list, median)
        print(low_num * high_num)


# 시간 초과
# import sys

# read = sys.stdin.readline
# n, q = map(int, read().split())
# n_list = list(map(int, read().split()))
# n_list.sort()
# median_list = [int(read()) for _ in range(q)]

# for median in median_list:
#     # 예외 조건
#     if median not in n_list or median == n_list[0] or median == n_list[-1]:
#         print('0')
#     # 가짓수 계산
#     else:
#         low_num = n_list.index(median)
#         high_num = n - low_num  - 1
#         print(low_num * high_num)
