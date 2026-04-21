n,k = map(int,input().split())

arr = list(map(int,input().split()))

q = []

answer = 0

for i in range(n):
  if i + k >= n: break
  tmp = int(1e9)
  for j in range(k):
    tmp = min(tmp,arr[i+j])
  answer = max(answer,tmp)

print(answer)