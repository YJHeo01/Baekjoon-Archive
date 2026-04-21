from collections import deque
from itertools import permutations

data = [1,2,3,4,5,6,7,8]

test_case_list = list(permutations(data,8))

n = int(input())

answer = 0

result = []

for _ in range(n):
    result.append(list(map(int,input().split())))

def get_line_up(test_case):
    line_up = []
    for i in range(3):
        line_up.append(test_case[i])
    line_up.append(0)
    for i in range(3,8):
        line_up.append(test_case[i])
    return line_up

for test_case in test_case_list:
    line_up = get_line_up(test_case)
    score = 0
    idx = 0
    for inning in range(n):
        out = 0
        queue = deque([0,0,0])
        while True:
            if out == 3:
                break
            player_name = line_up[idx]
            idx = (idx+1) % 9
            player_hit = result[inning][player_name]
            if player_hit == 0:
                out += 1
                continue
            queue.append(1)
            for _ in range(player_hit):
                score += queue.popleft()
            for _ in range(player_hit-1):
                queue.append(0)
    answer = max(answer,score)

print(answer)