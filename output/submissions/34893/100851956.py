u,o,s = map(int,input().split())

answer = 0

left = 0
right = u // 2

while left <= right:
  mid = (left+right)//2
  new_u = u - 2 * mid
  new_s = s + mid
  answer = max(answer,min(o,new_s,new_u))
  if new_u >= new_s:
    left = mid + 1
  else:
    right = mid - 1
    
print(answer)