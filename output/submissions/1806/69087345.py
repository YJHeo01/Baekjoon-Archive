n, c = map(int,input().split())

thing = list(map(int,input().split()))
answer = 100001
left = 0
right = 1
tmp = sum(thing[0:1])
while left < n and right < n and left<right:
    if tmp > c:
        tmp -= thing[left]
        answer = min(answer,(right-left))
        left += 1       
    else:
        tmp += thing[right]
        right+=1
    
if answer == 100001:
    answer = 0

print(answer)