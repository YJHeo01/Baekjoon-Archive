n = int(input())

points = []

for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(n):
        if tmp[j] == 1:
            points.append((i,j))
points_cnt = len(points)

def check_bissop(bishops,new_bishop):
    l = len(bishops)
    for i in range(l-1):
        if (bishops[i][0] == new_bishop[1] and new_bishop[0] == bishops[i][1]) or abs(bishops[i][0]-new_bishop[0]) == abs(bishops[i][1]-new_bishop[1]):
            return False
    return True
    
answer = 0

def backtracking(bishop_list,list_length,last_point_idx):
    global answer
    answer = max(answer,list_length)
    for i in range(last_point_idx+1,points_cnt):
        if check_bissop(bishop_list, points[i]):
            backtracking(bishop_list + [points[i]],list_length+1,i)

for i in range(points_cnt):
    backtracking([points[i]],1,i)

print(answer)