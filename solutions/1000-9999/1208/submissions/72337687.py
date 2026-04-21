n,s = map(int,input().split())

array = list(map(int,input().split()))

array.sort()

num_list = []

for i in range(n):
    if array[i] > s:
        n = i
        break
    num_list.append((i,array[i]))

answer = 0
while num_list != []:
    idx, value = num_list.pop()
    idx += 1
    if idx == n:
        if value == s:
            answer += 1
        continue
    if value > s:
        continue
    num_list.append((idx,value))
    if value + array[idx] <= s:
        num_list.append((idx,value+array[idx]))

print(answer)