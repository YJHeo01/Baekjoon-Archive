n,m = map(int,input().split())

def watch_cnt_search(graph,start,d):
    ret_v = 0
    vx = start[0]
    vy = start[1]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    while 1:
        vx = vx + dx[d]
        vy = vy + dy[d]
        if vx < 0 or vy < 0 or vx >= n or vy >= m or graph[vx][vy] == 6:
            return ret_v
        if graph[vx][vy] == 0:
            ret_v += 1
    return ret_v


def watch_start(graph,start,d):
    vx = start[0]
    vy = start[1]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    while 1:
        vx = vx + dx[d]
        vy = vy + dy[d]
        if vx < 0 or vy < 0 or vx >= n or vy >= m or graph[vx][vy] == 6:
            return
        if graph[vx][vy] == 0:
            graph[vx][vy] = -1
    return 0


ccty = []
room = []
for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(m):
        if tmp[j] not in (0,6):
            ccty.append((tmp[j],i,j))
    room.append(tmp)

ccty.sort(reverse=True)
abcd = 0

for i in ccty:
    abcd += 1
    if i[0] == 5:
        for j in range(4):
            watch_start(room,(i[1],i[2]),j)
    elif i[0] == 4:
        no = 0
        non_watch_idx = 0
        watch_cnt = [0] * 4
        for j in range(4):
            watch_cnt[j] = watch_cnt_search(room,(i[1],i[2]),j)
            if watch_cnt[non_watch_idx] > watch_cnt[j]:
                non_watch_idx = j
                no = 0
            elif watch_cnt[non_watch_idx] == watch_cnt[j]:
                no = 1
        if no == 1 and abcd <= 50:
            ccty.append(i)
            continue
        for j in range(4):
            if j == non_watch_idx:
                continue
            watch_start(room,(i[1],i[2]),j)
    elif i[0] == 3:
        no = 0
        watch_cnt = [0] * 4
        for j in range(4):
            watch_cnt[j] = watch_cnt_search(room,(i[1],i[2]),j)
            if watch_cnt[non_watch_idx] > watch_cnt[j]:
                non_watch_idx = j
                no = 0
            elif watch_cnt[non_watch_idx] == watch_cnt[j]:
                no = 1
        if no == 1 and abcd <= 50:
            ccty.append(i)
            continue    
        watch_idx = 0
        watch_idx_cnt = 0
        for j in range(4):
            tmp = watch_cnt[j] + watch_cnt[(j+1)%4]
            if watch_idx_cnt < tmp:
                watch_idx = j
                watch_idx_cnt = tmp
        watch_start(room,(i[1],i[2]),watch_idx)
        watch_start(room,(i[1],i[2]),(watch_idx+1)%4)
    elif i[0] == 2:
        watch_cnt = [0] * 4
        for j in range(4):
            watch_cnt[j] = watch_cnt_search(room,(i[1],i[2]),j)
        if watch_cnt[1] + watch_cnt[3] > watch_cnt[2] + watch_cnt[0]:
            watch_start(room,(i[1],i[2]),1)
            watch_start(room,(i[1],i[2]),3)
        elif watch_cnt[1] + watch_cnt[3] == watch_cnt[2] + watch_cnt[0] and abcd <= 50:
            ccty.append(i)
            continue
        else:
            watch_start(room,(i[1],i[2]),2)
            watch_start(room,(i[1],i[2]),0)
    elif i[0] == 1:
        no = 0
        max_idx = 0
        max_v = 0
        for j in range(4):
            tmp = watch_cnt_search(room,(i[1],i[2]),j)
            if tmp > max_v:
                max_v = tmp
                max_idx = j
                no = 0
            elif tmp == max_v:
                no = 1
        if no == 1 and abcd <= 50:
            ccty.append(i)
            continue
        watch_start(room,(i[1],i[2]),max_idx)
answer = 0
for i in range(n):
    for j in range(m):
        if room[i][j] == 0:
            answer += 1

print(answer)