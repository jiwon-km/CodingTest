# https://school.programmers.co.kr/learn/courses/30/lessons/12953
# 다시 풀어보기

from collections import Counter

def prime_factors(num):
    i = 2
    factors = []
    while i * i <= num:
        if num%i == 0:
            num //= i
            factors.append(i)
        else: i += 1
    factors.append(num)
    return factors


def solution(arr):
    answer = 1
    
    factors = [prime_factors(num) for num in arr]
    unique_factors=[]
    
    for factor in factors:
        uniq_fc = list((Counter(factor) - Counter(unique_factors)).elements())
        unique_factors += uniq_fc
        
    for f in unique_factors:
        answer *= f
        
    return answer
