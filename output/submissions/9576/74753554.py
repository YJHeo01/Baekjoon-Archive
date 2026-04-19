t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    book = [False] * (n+1)
    student = []
    answer = 0
    for _ in range(m):
        a,b = map(int,input().split())
        student.append((b,a))
    student.sort()
    for b,a in student:
        for i in range(a,b+1):
            if book[i] == False:
                book[i] = True
                answer += 1
                break
    print(answer)