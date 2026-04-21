import sys

input = sys.stdin.readline

import heapq

t = int(input())

for _ in range(t):
    stack = []
    n,k,ID,m = map(int,input().split())
    team_score_cnt = [[0]*(3+k) for _ in range(n+1)]
    my_team_score = 0
    my_team_cnt = 0
    for _ in range(m):
        i,j,s = map(int,input().split())
        if s > team_score_cnt[i][j]:
            team_score_cnt[i][k+1] = team_score_cnt[i][k+1] - team_score_cnt[i][j] + s
            team_score_cnt[i][j] = s
        team_score_cnt[i][k+2] += 1
        stack.append(i)
    heap = []
    for i in range(1,n+1):
        heapq.heappush(heap,(-team_score_cnt[i][k+1],team_score_cnt[i][k+2],i))
    same_my_team = 0
    dense_rank_team = []
    answer = 0
    while 1:
        if heap == []:
            break
        score, cnt, idx = heapq.heappop(heap)
        score = -score
        if score == team_score_cnt[ID][k+1] and cnt == team_score_cnt[ID][k+2]:
            same_my_team += 1
            dense_rank_team.append(idx)
        if same_my_team > 0 and (score != team_score_cnt[ID][k+1] or cnt != team_score_cnt[ID][k+2]):
            break
        answer += 1
    if same_my_team == 1:
        print(answer)
    else:
        tmp = []
        while 1:
            v = stack.pop()
            if v not in tmp and v in dense_rank_team:
                same_my_team -= 1
                if v == ID:
                    break
                tmp.append(v)
        answer += (same_my_team-1)
        print(answer)