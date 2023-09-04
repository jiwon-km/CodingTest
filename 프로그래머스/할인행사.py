# https://school.programmers.co.kr/learn/courses/30/lessons/131127

# 시간복잡도 O(len(discount) * len(want))
def solution(want, number, discount):
    total_num = sum(number)
    answer = 0

    window = discount[:total_num]
    counts = [window.count(item) for item in want]
    
    if counts == number:
        answer += 1
    
    for i in range(1, len(discount) - total_num + 1):
        if discount[i-1] in want:
            counts[want.index(discount[i-1])] -= 1
        if discount[i+total_num-1] in want:
            counts[want.index(discount[i+total_num-1])] += 1

        if counts == number:
            answer += 1
            
    return answer

# def solution(want, number, discount):
#     total_num = sum(number)
#     answer = 0
#     for i in range(len(discount)-total_num+1):
#         items = discount[i:i+total_num]
#         counts = [items.count(item) for item in want]

#         if counts == number:
#             answer += 1
        
#     return answer
           
