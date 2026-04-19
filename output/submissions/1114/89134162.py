l,k,c = map(int,input().split())

array = sorted(list(map(int,input().split())))

last_value = -1

pos = []

for i in array:
    if last_value == i: continue
    pos.append(i)
    last_value = i

k = len(pos)

pos.append(l)

def search_first_pos(value):
    first = l
    cnt = c
    for i in range(k-1,-1,-1):
        if first-pos[i] > value:
            if pos[i+1] - pos[i] > value: return -1
            cnt -= 1
            first = pos[i+1]
    if cnt > 0: first = pos[0]
    if first > value: return -1
    return first
    
left, right = 1,l

answer = l

while left < right:
    mid = (left+right) // 2
    if search_first_pos(mid) >= 1:
        answer = mid
        right = mid
    else:
        left = mid + 1

print(answer,search_first_pos(answer))    