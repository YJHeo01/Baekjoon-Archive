n = int(input())

array = list(map(int,input().split()))

pos = [0] * (n+1)

for i in range(n):
    pos[array[i]] = i + 1
    
answer = [0] * (n+1)

for i in range(1,n+1):
    answer[i] += abs(pos[i]-i)
    answer[array[i-1]] += abs(pos[array[i-1]]-pos[i])
    pos[array[i-1]] = pos[i]
    array[pos[i]-1] = array[i-1]

print(*answer[1:])