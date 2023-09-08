# https://school.programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, results):
    win_loss = [[0] * n for i in range(n)]
    for win, loss in results:
        win_loss[win-1][loss-1] = 1
        win_loss[loss-1][win-1] = -1 
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if win_loss[i][k] == 1 and win_loss[k][j] == 1:
                    win_loss[i][j] = 1
                elif win_loss[i][k] == -1 and win_loss[k][j] == -1:
                    win_loss[i][j] = -1
    
    cnt = 0
    for i in range(len(win_loss)):
        result = win_loss[i][:i] + win_loss[i][i+1:]
        if all(result):
            cnt += 1
                 
    return cnt
