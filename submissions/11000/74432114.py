import sys,heapq

input = sys.stdin.readline

n = int(input())

lecture_list = []

for _ in range(n):
    a,b = map(int,input().split())
    lecture_list.append((a,b))

lecture_list.sort()

finish_time_q = []

answer = 0
tmp = 0
for lecture in lecture_list:
    current_lecture_start, current_lecture_end = lecture
    while True:
        if finish_time_q == []:
            heapq.heappush(finish_time_q,current_lecture_end)
            tmp += 1
            answer = max(answer,tmp)
            break
        last_lecture_end = heapq.heappop(finish_time_q)
        if last_lecture_end <= current_lecture_start:
            tmp -= 1
        else:
            heapq.heappush(finish_time_q,last_lecture_end)
            heapq.heappush(finish_time_q,current_lecture_end)
            tmp += 1
            answer = max(tmp,answer)
            break

print(answer)