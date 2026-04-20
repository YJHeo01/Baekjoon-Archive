t = int(input())

for _ in range(t):
    n = int(input())
    rank_list = list(map(int,input().split()))
    team_cnt = max(rank_list)
    team_player_cnt = [0] * (team_cnt+1)
    team_score = [0] * (team_cnt+1)
    team_fifth_player = [0] * (team_cnt+1)
    for i in range(n):
        team_idx = rank_list[i]
        team_player_cnt[team_idx] += 1
        if team_player_cnt[team_idx] < 5:
            team_score[team_idx] += i
        elif team_player_cnt[team_idx] == 5:
            team_fifth_player[team_idx] = i
        else:
            continue
    correction_value = 0
    team_player_rank = [0] * (team_cnt+1)
    for i in range(n):
        team_idx = rank_list[i]
        if team_player_cnt[team_idx] < 6:
            correction_value += 1
        else:
            team_player_rank[team_idx] += 1
            if team_player_rank[team_idx] < 5:
                team_score[team_idx] -= correction_value
    
    winner_team_idx = -1
    winner_team_score = int(1e9)
    winner_team_fifth_player = int(1e9)
    for i in range(1,team_cnt+1):
        if team_player_cnt[i] < 6:
            continue
        if winner_team_score > team_score[i]:
            winner_team_idx = i
            winner_team_score = team_score[i]
            winner_team_fifth_player = team_fifth_player[i]
        elif winner_team_score == team_score[i] and team_fifth_player[i] < winner_team_fifth_player:
            winner_team_idx = i
            winner_team_fifth_player = team_fifth_player[i]
        else:
            continue
    print(winner_team_idx)