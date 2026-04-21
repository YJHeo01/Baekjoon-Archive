import sys

input = sys.stdin.readline

t = int(input())
INF = int(1e9)
for _ in range(t):
    n,m = map(int,input().split())
    students = []
    book_demand = [0] * (n+1)
    sold_out_book = [False] * (n+1)
    for _ in range(m):
        a,b = map(int,input().split())
        students.append((a,b))
        b+=1
        for i in range(a,b):
            book_demand[i] += 1
    answer = 0
    for student in students:
        book_idx = -1
        min_demand = INF
        for i in range(student[0],student[1]+1):
            if sold_out_book[i] == True:
                continue
            if min_demand > book_demand[i]:
                book_idx = i
                min_demand = book_demand[i]
            book_demand[i] -= 1
        if book_idx != -1:
            answer += 1
            sold_out_book[book_idx] = True
    print(answer)