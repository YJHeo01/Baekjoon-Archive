n = int(input())

tree_list = list(map(int,input().split()))

answer = 0

tree_list.sort(reverse=True)

for i in range(n):
    answer = max(answer,tree_list[i] + i)

answer += 2

print(answer)