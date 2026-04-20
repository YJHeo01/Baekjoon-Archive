t = int(input())

for _ in range(t):
    m,n,x,y = map(int,input().split())
    tmp = set([])
    answer = x
    visited = [False] * 40001
    while True:
        tmp = (answer-y) % n
        if tmp == 0: break
        answer += m
        if visited[tmp]:
            answer = -1
            break
        visited[tmp] = True
    print(answer)