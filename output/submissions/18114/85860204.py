n,c = map(int,input().split())
array = sorted(list(map(int,input().split())))
def backtracking(array,depth,vx,target_value,cur_value):
    if depth == 3: return
    for nx in range(vx+1,n):
        if array[nx] + cur_value == target_value:
            print(1)
            exit(0)
        if array[nx] + cur_value > target_value: return
        backtracking(array,depth+1,nx,target_value,cur_value+array[nx])

backtracking(array,0,-1,c,0)
print(0)