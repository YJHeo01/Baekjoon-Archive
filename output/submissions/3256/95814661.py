n = int(input())

r = [int(input()) for _ in range(n)]

time = [0] * 1001

for i in r:
    finish_time = -1
    for j in range(1,i+1):
        finish_time = max(finish_time,time[j])
        finish_time += 1
    time[i] = finish_time + 4
    
print(max(time))