INF = int(1e9)

l,k,c = map(int,input().split())
pos = sorted(list(map(int,input().split())))

first_answer = max(pos[0],l-pos[0])
second_answer = pos[0]

for i in range(k):
    x = pos[i]
    left, right = x, first_answer
    while left <= right:
        mid = (left+right) // 2
        cnt = c - 1
        last = x
        idx = i + 1
        while True:
            if idx == k or pos[idx] == l: break
            if cnt == 0:
                tmp = max(l - last,mid)
                if first_answer > tmp:
                    first_answer = tmp
                    second_answer = x
                break
            if pos[idx] - last > mid:
                cnt -= 1
                last = pos[idx - 1]
            else:
                idx += 1
        if idx == k or pos[idx] == l:
            right = mid - 1
            if first_answer > mid:
                first_answer = mid
                second_answer = x
        else:
            left = mid + 1

print(first_answer,second_answer)