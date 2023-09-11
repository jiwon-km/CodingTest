# https://school.programmers.co.kr/learn/courses/30/lessons/12911
# 1304-1313

def solution(input_number):
    result = 0
    binary_representation = bin(input_number)[2:]
    ones_count = binary_representation.count('1')
    
    while True:
        input_number += 1
        next_ones_count = bin(input_number)[2:].count('1')
        if ones_count == next_ones_count:
            break
        
    return input_number
