# https://school.programmers.co.kr/learn/courses/30/lessons/68645
# 삼각 달팽이
# 가독성+효율 고려해서 수정 예정


def solution(n):
    total_len = sum(range(1, n+1))
    empty_snail = [[0 for x in range(n) ]for x in range(n)]
    
    flag = 1
    i = 0
    j = 0
    n_i = [1, 0, -1] * (n+1 % 3)
    n_j = [0, 1, -1] * (n+1 % 3)
    iter_num = list(range(n, 0, -1))
    iter_num[0] -= 1
          
    for k in range(n):
        for _ in range(iter_num[k]):
            empty_snail[i][j] = flag
            flag += 1
            i += n_i[k]
            j += n_j[k]

    answer = []
    for k in range(n):
        for i in empty_snail[k][:k+1]:
            if i == 0:
                i = total_len
            answer.append(int(i))
    return answer
