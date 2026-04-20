n = int(input())

fruit = list(map(int,input().split()))

left,right = 0,0

answer = 0

tmp = 0

change_value_idx = 0
o = 0
while right < n:
    answer = max(answer,right-left+1)
    if fruit[left] != fruit[right]:
        if fruit[change_value_idx-1] == fruit[right]:
            change_value_idx = right
            o = 1
        else:
            if o == 0:
                change_value_idx += 1
            left = change_value_idx
    right += 1
    

print(answer)