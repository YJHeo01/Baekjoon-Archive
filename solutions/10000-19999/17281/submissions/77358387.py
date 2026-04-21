from itertools import permutations

data = [1,2,3,4,5,6,7,8]

test_case_list = list(permutations(data,8))

n = int(input())

answer = 0

result = []

for _ in range(n):
    result.append(list(map(int,input().split())))

for test_case in test_case_list:
    line_up = []
    for i in range(3):
        line_up.append(test_case[i])
    line_up.append(0)
    for i in range(3,8):
        line_up.append(test_case[i])
    score = 0
    idx = 0
    for inning in range(n):
        out = 0
        base = [False] * 4
        while True:
            player_name = line_up[idx]
            if result[inning][player_name] == 0:
                out += 1
                idx = (idx+1) % 9
                if out == 3:
                    break
                continue
            player_hit = result[inning][player_name]
            for i in range(3,-1,-1):
                if base[i] == False:
                    continue
                base[i] = False
                next_base = i + player_hit
                if next_base >= 4:
                    score += 1
                else:
                    base[next_base] = True
            idx = (idx+1) % 9
            if player_hit == 4:
                score += 1
            else:
                base[player_hit] = True
    answer = max(answer,score)
print(answer)