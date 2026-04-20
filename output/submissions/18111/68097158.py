def binary_search(n,ground,b_,length):
    answer = 0
    for i in range(length):
        if ground[i] < n:
            b_ = b_ - (n-ground[i])
            answer += (n-ground[i])
        else:
            b_ = b_ + (ground[i] - n)
            answer += 2 * (ground[i] - n)
    if b_ < 0:
        return -1
    else : return answer


n, m, b = map(int,input().split())
ground = []
for i in range(n):
    tmp = list(map(int,input().split()))
    ground += tmp

low = min(ground)
high = max(ground)
mn = m*n
h = low
answer = binary_search(low,ground,b,mn)
for i in range(low+1,high+1):
    tmp = binary_search(i,ground,b,mn)
    if tmp == -1:
        break
    if tmp <= answer:
        answer = tmp
        h = i
print(answer, h)