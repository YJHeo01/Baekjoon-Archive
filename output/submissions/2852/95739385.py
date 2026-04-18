n = int(input())

team_a_score = 0
team_b_score = 0

team_a_time = 0
team_b_time = 0

last_time = 0

for _ in range(n):
    idx, tmp = input().split()
    mm = tmp[:2]
    ss = tmp[3:]
    cur_time = 60 * int(mm) + int(ss)
    if team_a_score > team_b_score:
        team_a_time += (cur_time-last_time)
    if team_b_score > team_a_score:
        team_b_time += (cur_time-last_time)
    last_time = cur_time
    if idx == '1':
        team_a_score += 1
    else:
        team_b_score += 1
        
if team_a_score > team_b_score:
    team_a_time += (48 * 60-last_time)
else:
    team_b_time += (48*60-last_time)

if team_a_time//60<10:
    print('0',end="")
print(team_a_time//60,end=':')
if team_a_time%60<10:
    print('0',end="")
print(team_a_time%60)
if team_b_time//60<10:
    print('0',end="")
print(team_b_time//60,end=':')
if team_b_time%60<10:
    print('0',end="")
print(team_b_time%60)