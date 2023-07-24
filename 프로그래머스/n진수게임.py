# https://school.programmers.co.kr/learn/courses/30/lessons/17687
# n진수 게임

def print_arithmetic(n, num):
    ''' Input
      n (int): 진법 
      num (int) : 변환할 숫자
    '''
    alphabet_num = ['A', 'B', 'C', 'D', 'E', 'F']

    if n > num:
        if num >= 10:
            num = alphabet_num[num % 10]
        return str(num)

    answer = ''
    while num > 0:
        remainder = num % n

        if remainder >= 10:
            remainder = alphabet_num[remainder % 10]

        answer += str(remainder)
        num = num // n

    return answer[::-1]


def solution(n, t, m, p):
    number_list = '' 
    i = 0
    while len(number_list) < t * m:
        number_list += print_arithmetic(n, i)
        i += 1

    answer_of_tube = ''
    for i in range(t):
        answer_of_tube += number_list[i * m + (p - 1)]

    return answer_of_tube
