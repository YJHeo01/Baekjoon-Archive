dice = []

for i in range(3):
    dice.append(list(map(int,input().split())))

for i in range(3):
    winner = True
    for j in range(3):
        win_cnt = 0
        lose_cnt = 0
        if i == j: continue
        for k in range(6):
            for l in range(6):
                if dice[i][k] == dice[j][l]: continue
                if dice[i][k] > dice[j][l]: win_cnt += 1
                else: lose_cnt += 1
        if lose_cnt > win_cnt or win_cnt == 0: winner = False
    if winner >= True:
        print(i+1)
        exit(0)
        
print("No dice")