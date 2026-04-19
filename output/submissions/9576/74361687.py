import sys,heapq

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    book_list = [False] * (n+1)
    book_need_cnt = [0] * (n+1)
    student = []
    for _ in range(m):
        a,b = map(int,input().split())
        heapq.heappush(student,(b-a,a,b))
        for i in range(a,b+1):
            book_need_cnt[i] += 1
    answer = 0
    while student:
        book_range,a,b = heapq.heappop(student)
        book_idx = -1
        min_need_cnt = 1001
        for i in range(a,b+1):
            if book_list[i] == False:
                if min_need_cnt > book_need_cnt[i]:
                    book_idx = i
        if book_idx == -1:
            continue
        book_list[book_idx] = True
        book_need_cnt[book_idx] -= 1
        answer += 1
                
    print(answer)