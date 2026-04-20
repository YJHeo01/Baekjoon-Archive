w,n = map(int,input().split())

array = []

A = list(map(int,input().split()))

weight = [[] for _ in range(w)]

for i in range(n):
    for j in range(i):
        tmp = A[i] + A[j]
        if tmp >= w: continue
        weight[tmp].append((i,j))

left, right = 1,w-1

while left <= right:
    for a,b in weight[left]:
        for x,y in weight[right]:
            if a == x or b == y or a == y or b == x: continue
            print("YES")
            exit(0)
    left += 1; right -= 1
            
print("NO")