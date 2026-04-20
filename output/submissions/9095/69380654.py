t = int(input())

answer = [1]*(12)

answer[2], answer[3], answer[4] = 2,4,7

for i in range(5,12):
    answer[i] = answer[i-1] + answer[i-2] + answer[i-3]
for _ in range(t):
    n = int(input())
    print(answer[n])