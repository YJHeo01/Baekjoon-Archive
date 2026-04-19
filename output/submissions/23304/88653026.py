s = list(input())

length = len(s)

answer = "AKARAKA"

start_end = [(0,length-1),(0,length // 2 - 1),((length+1) // 2, length-1)]

for start,end in start_end:
    left, right = start,end

    while left <= right:
        if s[left] != s[right]:
            answer = "IPSELENTI"
        left += 1; right -= 1

print(answer)