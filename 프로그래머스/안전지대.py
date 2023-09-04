# https://school.programmers.co.kr/learn/courses/30/lessons/120866
# 1600-1607
# 3중 for문 ...

def solution(board):
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 0), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    
    n = len(board)
    cnt = 0
    
    for i in range(n):
        for j in range(n):
            # if any(board[i + dx][j + dy] for dx, dy in directions if 0 <= i + dx < n and 0 <= j + dy < n):
            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny]:
                    cnt += 1
                    break
                    
    return n * n - cnt
