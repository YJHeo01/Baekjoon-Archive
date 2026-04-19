from itertools import combinations

n,m,h = map(int,input().split())

ladder_matrix = [[False]*(h+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    ladder_matrix[b][a] = True

data = []

for i in range(1,n):
    for j in range(1,h+1):
        if ladder_matrix[i][j] == True:
            continue
        data.append((i,j))

answer = -1

def solution(graph,start):
    x,y = start
    while True:
        if graph[x][y] == True:
            while True:
                x += 1
                if graph[x][y] == False:
                    break
            y += 1
        elif graph[x-1][y] == True:
            while True:
                x -= 1
                if graph[x-1][y] == False:
                    break
            y += 1
        else:
            y += 1
        if y > h:
            break
    if start[0] == x:
        return True
    return False



for i in range(4):
    test_case_list = list(combinations(data,i))
    for test_case in test_case_list:
        success = True
        for x,y in test_case:
            ladder_matrix[x][y] = True
        for k in range(1,n+1):
            success = solution(ladder_matrix,(k,0))
            if success == False:
                break
        if success == True:
            answer = i
            break
        for x,y in test_case:
            ladder_matrix[x][y] = False
    if answer != -1:
        break
print(answer)