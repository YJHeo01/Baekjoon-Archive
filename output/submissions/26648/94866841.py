n = int(input())

arr = [list(map(int,input().split())) for _ in range(3)]

answer = 'YES'

cur_value = -1

for i in range(n):
    tmp = sorted([arr[0][i],arr[1][i],arr[2][i]])
    if tmp[2] <= cur_value:
        answer = "NO"
        break
    cur_value = max(cur_value+1,tmp[0])

print(answer)