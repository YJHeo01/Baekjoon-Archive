n = int(input())

r = [int(input()) for _ in range(n)]

time = [0] * 1001

for i in r:
    finish_time = 0
    for j in range(1,i):
        finish_time = max(finish_time,time[j])
        finish_time += 1
    finish_time = max(finish_time,time[i])
    time[i] = finish_time + 5
    
print(max(time))