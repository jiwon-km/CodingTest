# https://school.programmers.co.kr/learn/courses/30/lessons/42888
# 오픈채팅방

def solution(records):
    # 필요한 데이터 1) uid-닉네임 딕셔너리 2) 채팅방 입출 로그
    
    result_action = {'Enter' : '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    
    logs = []
    # 1. uid-닉네임 매칭
    uid_nickname = {}
    for record in records:
        if record.split(' ')[0] != 'Leave':
            uid, nickname = record.split(' ')[1], record.split(' ')[2]
            uid_nickname[uid] = nickname
    
    # 2. 채팅방 입출 로그 작성
    for record in records:
        if record.split(' ')[0] != 'Change':
            action, new_uid = record.split(' ')[0], record.split(' ')[1]
            answer = uid_nickname[new_uid]+result_action[action]
            logs.append(answer)
            
    return logs
