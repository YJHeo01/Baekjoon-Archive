n,m,q = map(int,input().split())

time = [0] * (n+1)

correct = [[False]*(m+1) for _ in range(n+1)]

wrong_cnt = [[0]*(m+1) for _ in range(n+1)]

for _ in range(q):
    t, t_idx, p_idx, result = input().split()
    t = int(t); t_idx = int(t_idx); p_idx = int(p_idx)
    if correct[t_idx][p_idx]: continue
    if result == "AC":
        correct[t_idx][p_idx] = True
        time[t_idx] += t
        time[t_idx] += wrong_cnt[t_idx][p_idx] * 20
    else:
        wrong_cnt[t_idx][p_idx] += 1
    
rank = []

for i in range(1,n+1):
    score = sum(correct[i])
    rank.append((score,time[i],i))
    
rank.sort(key=lambda x:(-x[0],x[1],x[2]))

for team in rank:
    print(team[2],team[0],team[1])