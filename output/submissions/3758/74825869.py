import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,k,t,m = map(int,input().split())
    team_problem_score = [[0]*(k+1) for _ in range(n+1)]
    team_submit_cnt = [0] * (n+1)
    team_submit_last_time = [0] * (n+1)
    for time in range(m):
        i,j,s = map(int,input().split())
        team_submit_cnt[i] += 1
        team_submit_last_time[i] = time
        team_problem_score[i][j] = max(s,team_problem_score[i][j])
    team_score = [0] * (n+1)
    for i in range(n+1):
        team_score[i] = sum(team_problem_score[i])
    team_information = []
    for i in range(1,n+1):
        team_information.append((-team_score[i],team_submit_cnt[i],team_submit_last_time[i],i))
    team_information.sort()
    answer = 0
    for rank in range(n):
        score, submit_cnt, last_time, team_idx = team_information[rank]
        if team_idx == t:
            answer = rank + 1
            break
    print(answer)