#  https://softeer.ai/practice/info.do?idx=1&eid=392

# 시간 초과 이유 : 현재 강의에 대해 다음 강의를 찾기 위해 나머지 모든 강의를 검사 => O(n^2)
# 수정 : 다음 강의 찾았을 때, 바로 반복문 탈출해서 불필요한 연산 줄임

import sys

read = sys.stdin.readline

n = int(read())
time_list = [list(map(int, read().split())) for _ in range(n)]
time_list.sort(key = lambda x :x[1])

cnt = 1
idx = 0

while idx < len(time_list) - 1:
    f_lecture = time_list[idx]
    # 시작시간이 종료시간보다 작은 강의 제거 -> 가장 빠른 종료 시간 채택
    for i in range(idx + 1, len(time_list)):
        if time_list[i][0] >= f_lecture[1]:
            idx = i
            cnt += 1
            break
    else:
        break

print(cnt)


#  시간 초과

# import sys

# read = sys.stdin.readline

# n = int(read())
# time_list = [list(map(int, read().split())) for _ in range(n)]
# time_list.sort(key = lambda x :x[1])

# cnt = 1
# idx = 0

# while True:
#     # 종료조건
#     if idx == len(time_list)-1:
#         break

#     f_lecture = time_list[idx]
#     # 시작시간이 종료시간보다 작은 강의 제거 -> 가장 빠른 종료 시간 채택
#     for i in range(idx+1, len(time_list)):
#         if time_list[i][0] < f_lecture[1]:
#             continue
#         else:
#             idx = i
#             cnt += 1
#             break

# print(cnt)
