n,k = map(int,input().split())
array = sorted(list(map(int,input().split())))
answer = 0
 
while array:
    tmp = array.pop()
    if tmp < k:
        array.append(tmp)
        break
    answer += 1
 
left, right = 0, n-answer-1
 
while left < right:
    if array[left] + array[right] >= k:
        right -= 1
        answer += 1
    left += 1
 
if answer == 0: answer = -1
print(answer)