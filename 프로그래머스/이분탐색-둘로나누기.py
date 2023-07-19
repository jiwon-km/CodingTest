# 전력망을 둘로 나누기
# https://school.programmers.co.kr/learn/courses/30/lessons/86971
# 다시 풀 예정


def cut_and_calc_wire(wires, i):
    cutted_wires = wires[:i] + wires[i+1:]
    wire_1 = set([cutted_wires[0][0]])

    while True:
        added = False
        for wire in cutted_wires:
            if wire[0] in wire_1 and wire[1] not in wire_1:
                wire_1.add(wire[1])
                added = True
            elif wire[1] in wire_1 and wire[0] not in wire_1:
                wire_1.add(wire[0])
                added = True
        if not added:
            break
    return list(wire_1)


def solution(n, wires):
    ans_arr = []
    for i in range(len(wires)):
        wire_set_1 = cut_and_calc_wire(wires, i)
        wire_set_1 = list(set(wire_set_1))
        
        num_wire1 = len(wire_set_1)
        num_wire2 = n - num_wire1
        ans_arr.append(max(num_wire2, num_wire1) - min(num_wire2, num_wire1))

    return min(ans_arr)
