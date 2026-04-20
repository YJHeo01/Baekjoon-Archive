from itertools import combinations

data = []

n,m,d = map(int,input().split())

game = []

for _ in range(n):
    game.append(list(map(int,input().split())))

for i in range(m):
    data.append(i)

test_case = list(combinations(data,3))
answer = 0

for case in test_case:
    tmp = 0
    archer_y = n-1
    killed_enermy = []
    for i in range(n):
        target_enermy = []
        for archer_x in case:
            decide_kill = False
            for j in range(d):
                if decide_kill == True:
                    break
                for k in range(-j,j+1):
                    nx = archer_x + k
                    ny = archer_y - (j-abs(k))
                    if ny < 0 or nx < 0 or nx >= m:
                        continue
                    if game[ny][nx] == 1:
                        target_enermy.append((ny,nx))
                        decide_kill = True
                        break
        for enermy_y, enermy_x in target_enermy:
            if game[enermy_y][enermy_x] == 1:
                killed_enermy.append((enermy_y,enermy_x))
                game[enermy_y][enermy_x] = 0
                tmp += 1
        archer_y -= 1
    for y,x in killed_enermy:
        game[y][x] = 1
    answer = max(tmp,answer)

print(answer)