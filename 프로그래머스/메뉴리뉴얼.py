# https://school.programmers.co.kr/learn/courses/30/lessons/72411
# 1323-1400
# 복잡하게도 풀었다. Counter 사용하여 다시 풀 예정
# issubset 사용하면 간결하다

from itertools import combinations

def extract_combinations(order, n):
    return [''.join(sorted(comb)) for comb in combinations(order, n)]

def solution(orders, course):
    answer = []

    for num in course:
        all_combinations = [comb for order in orders for comb in extract_combinations(order, num)]
        unique_combinations = list(set(all_combinations))
        count = [0] * len(unique_combinations)

        for i, comb in enumerate(unique_combinations):
            for order in orders:
                if set(comb).issubset(order):
                    count[i] += 1
                    
        max_count = max(count, default=0)
        if max_count >= 2:
            answer.extend([comb for i, comb in enumerate(unique_combinations) if count[i] == max_count])
    
    answer.sort()
    return answer

# from itertools import combinations

# def extract_candidate(order, n):
#     candidate = list(combinations(order, n))
#     n_order_list = []
#     for can in candidate:
#         res = ''    
#         for i in can:
#             res += i
#         n_order_list.append(res)
#     return n_order_list

# def contains_all_chars(main_string, chars):
#     return all(char in main_string for char in chars)

# def remove_if_reversed_exists_and_sort(lst):
#     # 문자열 내의 문자를 정렬
#     lst = [''.join(sorted(item)) for item in lst]
    
#     for item in lst[:]:
#         if item[::-1] in lst:
#             lst.remove(item)
#     lst = list(set(lst))
#     return lst

# def solution(orders, course):
#     answer = []
    
#     for num in course:
#         candidate = []
#         for order in orders:
#             candidate += extract_candidate(order, num)
#         candidate = list(set(candidate))
#         cnt = [0] * len(candidate)

#         for i in range(len(candidate)):
#             for order in orders:
#                 if contains_all_chars(order, candidate[i]):
#                     cnt[i] += 1
#         if cnt:
#             max_cnt = max(cnt)
#             if max_cnt >= 2:
#                 for i in range(len(cnt)):
#                     if cnt[i] == max_cnt:
#                         answer.append(candidate[i])
    
#     answer = remove_if_reversed_exists_and_sort(answer)            
#     answer.sort()  
#     return answer

