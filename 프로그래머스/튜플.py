# https://school.programmers.co.kr/learn/courses/30/lessons/64065
# 튜플

def solution(s):
    answer = []
    
    num_list = []
    s_split_list = s.split('},{')
    
    if len(s_split_list) == 1:
        return [int(s_split_list[0][2:-2])]

    for i in range(len(s_split_list)):
        if i == 0 :
            num_list.append(s_split_list[i][2:])
        elif i == len(s_split_list)-1:
            num_list.append(s_split_list[i][:-2])
        else:
            num_list.append(s_split_list[i][:])
            
    num_list.sort(key=len)

    answer.append(int(num_list[0]))
    for i in range(1, len(num_list)):
            res = list(set(str(num_list[i]).split(',')) - set(str(num_list[i-1]).split(',')))
            answer.append(int(res[0]))
            
    return answer
