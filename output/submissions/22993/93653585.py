n = int(input())

arr = list(map(int,input().split()))

junie = arr[0]

arr = sorted(arr[1:])

answer = 'Yes'

for i in arr:
    if junie > i:
        junie += i
    else:
        answer = 'No'
        
print(answer)