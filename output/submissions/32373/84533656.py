n,k = map(int,input().split())

array = list(map(int,input().split()))

for start in range(k):
    for end in range(n-1,-1,-k):
        for right in range(start+k,end,k):
            left = right - k
            if array[left] > array[right]: 
                array[left], array[right] = array[right], array[left]
answer = 'Yes'

for i in range(n):
    if array[i] != i:
        answer = 'No'

print(answer)