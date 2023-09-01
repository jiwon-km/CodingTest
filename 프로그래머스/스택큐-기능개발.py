# https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    is_done = [False] * len(progresses)
    answer = []
    
    while not all(is_done):
        # 1. progress update
        progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]
        # 2. progress check
        is_done = [True if progress >= 100 else is_done[i] for i, progress in enumerate(progresses)]
      
        # 3. confirm release
        for i, flag in enumerate(is_done):
            if not flag:
                progresses = progresses[i:]
                is_done = is_done[i:]
                speeds = speeds[i:]
                if i: answer.append(i)
                break
        
    answer.append(len(is_done))
    return answer
    
