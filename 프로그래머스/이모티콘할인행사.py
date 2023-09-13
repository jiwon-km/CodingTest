# https://school.programmers.co.kr/learn/courses/30/lessons/150368
# 1308 - 1349
# 조건을 잘 읽자 "이모티콘마다 할인율은 다를 수 있으며, 할인율은 10%, 20%, 30%, 40% 중 하나로 설정됩니다."
# TC15번 실패 : 부동소수점오차 => 20번 라인 추가

import itertools

def solution(users, emoticons):
    answer = []
    discount_ratio = [0.9, 0.8, 0.7, 0.6]
    discount_lst = list(itertools.product(discount_ratio, repeat = len(emoticons)))
    
    for discount in discount_lst:
        total_money = 0
        ppl = 0
        for user in users:
            money = 0
            for i in range(len(emoticons)):
                # 구매 여부 확인
                dscnt_ratio = int((1 - discount[i]) * 100 + 0.5)
                if dscnt_ratio >= user[0]:
                    money += discount[i] * emoticons[i]
            # 가입 여부 확인
            if money >= user[1]:
                money = 0
                ppl += 1
            total_money += money
        
        answer.append([ppl, total_money])
        
    return max(answer)
