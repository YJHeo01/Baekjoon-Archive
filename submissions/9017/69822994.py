INF = int(1e9)

t = int(input())

for _ in range(t):
    n = int(input())
    test_case = list(map(int,input().split()))
    size = max(test_case)+1
    team_score = [[] for _ in range(size)]
    real_team = []
    real_team_size = 0
    team_player = [0]*(size)
    for i in range(n):
        team_score[test_case[i]].append(i+1)
        team_player[test_case[i]]+=1
        if team_player[test_case[i]] == 6:
            real_team.append(test_case[i])
            real_team_size += 1
    real_team_score = [0] * size
    real_team_idx = [0] * size
    l = real_team_size * 4
    i = 1
    while 1:
        idx = -1
        for j in real_team:
            if real_team_idx[j] >=4:
                continue
            if idx == -1:
                idx = j
            else:
                if team_score[idx][real_team_idx[idx]] > team_score[j][real_team_idx[j]]:
                    idx = j
        if idx == -1:
            break
        real_team_score[idx] += i
        real_team_idx[idx] += 1
        i += 1
    


    answer_team = 0
    answer_score = INF
    for i in real_team: 
        if real_team_score[i] < answer_score:
            answer_score = real_team_score[i]
            answer_team = i
        elif real_team_score[i] == answer_score:
            if team_score[i][4] < team_score[answer_team][4]:
                answer_team = i
    print(answer_team)