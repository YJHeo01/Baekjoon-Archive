t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    book = [False] * (n+1)
    student = []
    idx_start = [0] * (n+1)
    answer = 0
    for i in range(n+1):
        idx_start[i] = i
    for _ in range(m):
        a,b = map(int,input().split())
        prior = b-a
        student.append((prior,a,b))
    for prior,a,b in student:
        if idx_start[a] > b:
            continue
        for i in range(idx_start[a],b+1):
            if book[i] == False:
                book[i] = True
                idx_start[a] = i+1
                answer += 1
                break
    print(answer)