n,m,r = map(int,input().split())

teams = []

for i in range(n):
    teams.append(list(input())+[i+1])

cnt = 0

for i in range(n):
    for j in range(m):
        if teams[i][j] == 'P': cnt += 1

def sol(va):
    for i in range(n-1,-1,-1):
        for j in range(m):
            if teams[i][j] != 'P': continue
            if teams[i][j] == 'P':
                if va[-1] == '.':
                    teams[i][j] = 'R'
                else:
                    teams[i][j] = 'A'
                    y_cnt = 0
                    for c in va:
                        if c == 'y': y_cnt += 1
                    y_cnt -= 3
                    for k in range(y_cnt):
                        teams[i-k], teams[i-k-1] = teams[i-k-1], teams[i-k]
            return

for _ in range(cnt):
    oh, va = input().split()
    sol(va)
            

for i in range(n):
    if teams[i][-1] == r:
        print(i+1)