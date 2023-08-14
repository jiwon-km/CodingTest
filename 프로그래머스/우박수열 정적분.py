# https://school.programmers.co.kr/learn/courses/30/lessons/134239

# 수정사항 : 간략화
def make_Collatz_Sequence(num):
    collatz_seq = [num]
    while num != 1:
        num = num // 2 if num % 2 == 0 else num * 3 + 1
        collatz_seq.append(num)
    return collatz_seq

def solution(k, ranges):
    collatz_seq = make_Collatz_Sequence(k)
    n = len(collatz_seq)
    answer = []
    
    for a, offset in ranges:
        b = n + offset
        if a >= b:
            answer.append(-1)
        else:
            area = sum((collatz_seq[i] + collatz_seq[i+1]) * 0.5 for i in range(a, b-1))
            answer.append(area)
        
    return answer


# def make_Collatz_Sequence(num):
#     collatz_seq = []
#     collatz_seq.append(num)
#     while True:
#         if num % 2 == 0:
#             num = num//2
#         else:
#             num = num * 3 + 1
#         collatz_seq.append(num)
#         if num == 1:
#             break
#     return collatz_seq

# def solution(k, ranges):
#     collatz_seq = make_Collatz_Sequence(k)
#     n = len(collatz_seq)
#     answer = []
    
#     for rang in ranges:
#         area = 0
#         a = rang[0]
#         b = n + rang[1]

#         if a >= b:  # enable
#             answer.append(-1)
#         else:
#             for i in range(a, b-1):
#                 area += (collatz_seq[i] + collatz_seq[i+1]) * 0.5
#             answer.append(area)
        
#     return answer
