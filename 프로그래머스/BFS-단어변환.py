# 문제 풀이 일자 : 7월 13일
# 해결 여부 : △
# 첫 번째 접근 방법 : 가능한 알파벳들의 사전을 만들어서, 그 내에서 조합을 검사하려고 했지만 사전의 알파벳에 원래 단어 인덱스도 같이 저장되고 처리되어야 할 것 같아서 패스
# 두 번째 접근 방법 : BFS로 접근하여 단어들에 하나씩 접근하여 살펴보되, is_one_char_different라는 함수를 정의하여 한 글자 다른지 여부 체크. visited를 어떻게 구성해야 할 지 몰랐음

from collections import deque

def is_one_char_different(word1, word2):
    diff_count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff_count += 1
            if diff_count > 1:
                return False
    return True


def solution(begin, target, words):
    # 종료 조건
    if target not in words:
        return 0

    queue = deque()
    queue.append((begin, 0))  # 단어, 변환 횟수
    visited = set() # visited의 shape을 len(begin) x len(words)로 해야하는지 고민했음, 하지만 set에 이미 본 단어들을 저장하는 식으로 visited 구성
    visited.add(begin)
    
    while queue:
        current_word, count = queue.popleft()

        if current_word == target:
            return count

        for word in words:
            if word not in visited and is_one_char_different(current_word, word):
                queue.append((word, count + 1))
                visited.add(word)

    return 0
