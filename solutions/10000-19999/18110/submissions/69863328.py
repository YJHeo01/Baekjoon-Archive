import sys

input = sys.stdin.readline

n = int(input())

num_list = []

for _ in range(n):
    num_list.append(int(input()))

num_list.sort()

cut_off = round(n * 3 / 20)
if n != 0:
    answer = round(sum(num_list[cut_off:n-cut_off]) / (n - 2*cut_off))
else:
    answer=0

print(answer)