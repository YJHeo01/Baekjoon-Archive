rect = [list(input()) for _ in range(10)]

answer = 1000

for i in range(1<<10):
    r = []
    for k in range(10):
        if i % 2 == 1:
            r.append(k)
        i //= 2
    for j in range(1<<10):
        tmp = []
        c = []
        for k in range(10):
            tmp.append(rect[k])
            if j % 2 == 1:
                c.append(k)
            j //= 2
        if len(r) * len(c) >= answer: continue
        for x in r:
            for y in c:
                for dx,dy in [(0,0),(0,-1),(-1,0),(1,0),(0,1)]:
                    nx = x + dx
                    ny = y + dy
                    if nx < 0 or ny < 0 or nx >= 10 or ny >= 10: continue
                    if tmp[nx][ny] == '#':
                        tmp[nx][ny] = 'O'
                    else:
                        tmp[nx][ny] = '#'
        bol = True
        for row in tmp:
            for column in row:
                if column == '#':
                    bol = False
        if bol: answer = len(r) * len(c)
        
if answer == 1000: answer = -1
                
print(answer)