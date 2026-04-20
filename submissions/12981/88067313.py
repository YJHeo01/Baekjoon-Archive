array = sorted(list(map(int,input().split())))
answer = array[0]

for i in range(3): array[i] -= answer
answer += array[1] // 3
answer += array[2] // 3
answer += max(array[1]%3,array[2]%3)
if max(array[1]%3,array[2]%3) == 2 and min(array[1]%3,array[2]%3) == 0:answer -= 1

print(answer)