n,k,t = map(int,input().split())
array = list(map(int,input().split()))
eat = [False] * n
array.sort()
cur_idx = 0
last_idx = -1
for _ in range(k):
    while True:
        if eat[n-1] == True:
            while True:
                if last_idx == -1: break
                if array[last_idx] == False:
                    break
                last_idx -= 1
            t += array[last_idx]
            eat[last_idx] = True
            break
        elif cur_idx == n or array[cur_idx] >= t:
            last_idx = cur_idx - 1
            while True:
                if last_idx == -1 or eat[last_idx] == False: break
            break
        else:
            cur_idx += 1
    if last_idx == -1: break
    t += array[last_idx]
    eat[last_idx] = True
print(t)