n,x,y,z = map(int,input().split())
 
left, right = 1,10**18
 
target_time = right
 
cnt = n + 3
while left <= right:
    mid = (left+right) // 2
    tmp = mid // x + mid // y + mid // z
    if tmp >= n:
        target_time = mid
        right = mid - 1
        cnt = tmp
    else:
        left = mid + 1
 
answer = ['A','B','C']
last_time_A, last_time_B, last_time_C = x * (target_time//x), y * (target_time//y), z * (target_time//z)
time_list = sorted([[last_time_A,0],[last_time_B,1],[last_time_C,2]])
print(answer[time_list[2-cnt+n][1]],end=" ")
print("win")