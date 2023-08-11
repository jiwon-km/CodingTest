# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    past_word = set()
    before_word = words[0]
    past_word.add(words[0])
    words = words[1:]

    for idx, word in enumerate(words, start=1):
        # 조건 1: 이미 나온 단어인지 확인
        if word in past_word:
            return [idx % n + 1, idx // n + 1]

        # 조건 2: 끝말잇기 조건 확인
        if before_word[-1] != word[0]:
            return [idx % n + 1, idx // n + 1]

        past_word.add(word)
        before_word = word

    return [0, 0]
