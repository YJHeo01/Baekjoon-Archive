n,k = map(int,input().split())

array = list(map(int,input().split()))

answer = 0

for i in range(1000,0,-1):
    basket_cnt = 0
    for j in array:
        basket_cnt += j // i
        if j % i != 0: basket_cnt += 1
    if basket_cnt < k: continue
    tmp = 0
    num_list = []
    for j in array:
        num_list += [i] * (j//i)
        num_list.append(j%i)
    num_list.sort()
    for _ in range(k//2): num_list.pop()
    for _ in range(k//2): tmp += num_list.pop()
    answer = max(answer,tmp)

print(answer)