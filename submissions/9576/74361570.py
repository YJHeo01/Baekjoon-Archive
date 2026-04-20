import sys,heapq

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    book = [False] * (n+1)
    student = []
    for _ in range(m):
        a,b = map(int,input().split())
        heapq.heappush(student,(b-a,a,b))
    answer = 0
    while student:
        book_range,a,b = heapq.heappop(student)
        for i in range(a,b+1):
            if book[i] == False:
                book[i] = True
                answer += 1
                break
    print(answer)
