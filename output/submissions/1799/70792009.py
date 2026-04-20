n = int(input())

points = []
points_cnt = 0
for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(n):
        if tmp[j] == 1:
            points.append((i,j))
            points_cnt += 1

def check_bishop(bishops,new_bishop):
    for bishop in bishops:
        if (bishop[0] == new_bishop[1] and new_bishop[0] == bishop[1]) or abs(bishop[0]-new_bishop[0]) == abs(bishop[1]-new_bishop[1]):
            return False
    return True
    
answer = 0

def backtracking(bishop_list,list_length,last_point_idx):
    ret_v = list_length
    for i in range(last_point_idx+1,points_cnt):
        if check_bishop(bishop_list, points[i]):
            visited[i] = True
            ret_v = max(backtracking(bishop_list + [points[i]],list_length+1,i),ret_v)
    return ret_v

visited = [False] * points_cnt
for i in range(points_cnt):
    if visited[i] == True:
        continue
    answer = max(answer,backtracking([points[i]],1,i))
    visited[i] = True

print(answer)