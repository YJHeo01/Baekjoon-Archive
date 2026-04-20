import sys

input = sys.stdin.readline

n = int(input())

num_list = [0]

for _ in range(n):
    num_list.append(int(input()))

num_list.sort()

answer = 0

for i in range(1,n+1):
    answer += abs(num_list[i] - i)

print(answer)