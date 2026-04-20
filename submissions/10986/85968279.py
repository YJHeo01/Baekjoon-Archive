n,m = map(int,input().split())
array = list(map(int,input().split()))
mod_value_cnt = [0] * m
tmp = 0
answer = 0
for i in range(n):
    tmp += array[i]
    tmp %= m
    if tmp == 0: answer += 1
    mod_value_cnt[tmp] += 1
for i in range(m):
    answer += mod_value_cnt[i] * (mod_value_cnt[i]-1) // 2

print(answer)