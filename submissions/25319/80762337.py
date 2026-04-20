from collections import deque

def main():
    n,m,s_length = map(int,input().split())
    graph = []
    all_alphbet_cnt = {}
    target_alphbet_cnt = {}
    for _ in range(n):
        graph.append(list(input()))
    alphabet_position ={}
    for i in range(n):
        for j in range(m):
            if graph[i][j] in all_alphbet_cnt:
                all_alphbet_cnt[graph[i][j]] += 1
                alphabet_position[graph[i][j]].append((i,j))
            else:
                all_alphbet_cnt[graph[i][j]] = 1
                alphabet_position[graph[i][j]] = deque([(i,j)])
                
    s = list(input())

    for c in s:
        if c not in target_alphbet_cnt:
            target_alphbet_cnt[c] = 1
        else:
            target_alphbet_cnt[c] += 1
    C = int(1e9)
    for c in s:
        C = min(C,all_alphbet_cnt[c]//target_alphbet_cnt[c])
    print(C,end=" ")
    path = deque([(0,0)])
    for _ in range(C):
        for c in s:
            if c not in alphabet_position:
                path = deque([0,0])
                break
            path.append(alphabet_position[c].popleft())
    path.append((n-1,m-1))
    solution(path)

def solution(path):
    move_cnt = 0
    sentence = ""
    vx,vy = path.popleft()
    nx,ny = path.popleft()
    while path:
        
        if vx == nx and vy == ny:
            sentence += 'P'
            move_cnt += 1
            nx,ny = path.popleft()
                
        if vx > nx:
            move_cnt += 1
            vx -= 1
            sentence += 'U'
        if vx < nx:
            move_cnt += 1
            vx += 1
            sentence += 'D'
            
        if vy > ny:
            move_cnt += 1
            vy -= 1
            sentence += 'L'
        if vy < ny:
            move_cnt += 1
            vy += 1
            sentence += 'R' 
    
    while True:
        if vx == nx and vy == ny:
            break
        if vx > nx:
            move_cnt += 1
            vx -= 1
            sentence += 'U'
        if vx < nx:
            move_cnt += 1
            vx += 1
            sentence += 'D'
            
        if vy > ny:
            move_cnt += 1
            vy -= 1
            sentence += 'L'
        if vy < ny:
            move_cnt += 1
            vy += 1
            sentence += 'R' 

    print(move_cnt)
    print(sentence)        


if __name__ == "__main__":
    main()