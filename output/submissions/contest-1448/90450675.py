a,b = map(int,input().split())

n = int(input())

target = a - b

if target < 0:
    print(1,1)
    exit(0)

answer_l, answer_r = -1,-1

array = [list(map(int,input().split())) for _ in range(n)]

l = []

r = []

for i in range(n):
    tmp_a, tmp_b = array[i]
    l.append((tmp_a,i+1))
    r.append((tmp_b,i+1))
    
cur_value = int(1e19)

for i in range(n):
    if array[i][0] > target and array[i][0] < cur_value:
        answer_l, answer_r = i+1,-1
        cur_value = array[i][0]
    if array[i][1] > target and array[i][1] < cur_value:
        answer_l, answer_r = -1,i+1
        cur_value = array[i][1]

l.sort(); r.sort()

left, right = 0,n-1

while True:
    if right < 0 or left >= n: break
    if l[left][0] + r[right][0] <= target:
        left += 1
    else:
        if l[left][0] + r[right][0] < cur_value and l[left][1] != r[right][1]:
            answer_l, answer_r = l[left][1], r[right][1]
        right -= 1
        
left, right = 0,n-1

while True:
    if right < 0 or left >= n: break
    if l[right][0] + r[left][0] <= target:
        left += 1
    else:
        if l[right][0] + r[left][0] < cur_value and l[right][1] != r[left][1]:
            answer_l, answer_r = l[right][1],r[left][1]
        right -= 1

if answer_l == -1 and answer_r == -1:
    print("No")
else:
    print(answer_l,answer_r)