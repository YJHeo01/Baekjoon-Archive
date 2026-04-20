INF = 1000001

n = int(input())

num_list = list(map(int,input().split()))

answer = [0] * 21

for i in num_list:
    tmp = i
    for j in range(20):
        if tmp & 1 != 0:
            answer[j] += 1
        tmp >>= 1

print(max(answer))