# https://school.programmers.co.kr/learn/courses/30/lessons/138476
# 이진분할보다 딕셔너리 기반 접근 방법이 훨씬 효율적이다
# 정렬할 때 O(M log M), 이진분할 할 때 O(N log M).. , 반면 딕셔너리는 O(M)

import bisect

def solution(k, tangerine):
    tangerine.sort()
    unique_tangerines = list(set(tangerine))

    count_list = []
    for tang_type in unique_tangerines:
        left_index = bisect.bisect_left(tangerine, tang_type)
        right_index = bisect.bisect_right(tangerine, tang_type)
        count_list.append(right_index - left_index)
   
    # type_counts = {}
    # for tang in tangerine:
    #     type_counts[tang] = type_counts.get(tang, 0) + 1
        
        
    count_list.sort(reverse=True)

    total_count = 0
    num_types = 0
    for count in count_list:
        total_count += count
        num_types += 1
        if total_count >= k:
            break
    
    return num_types
