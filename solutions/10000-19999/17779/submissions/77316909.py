n = int(input())

city = []

for _ in range(n):
    city.append(list(map(int,input().split())))

def get_fifth_area_poplutaion(city,visited,x,height,left,right):
    ret_value = 0
    for i in range(height):
        row = x + i
        for column in range(left[i],right[i]+1):
            visited[row][column] = True
            ret_value += city[row][column]
    return ret_value

def get_population(city,visited,x1,y1,x2,y2):
    ret_value = 0
    for i in range(x1,x2):
        for j in range(y1,y2):
            if visited[i][j] == True:
                continue
            ret_value += city[i][j]
    return ret_value

def get_left_list(y,d1,d2):
    left = []
    for i in range(d1):
        left.append(y-i)
    for i in range(d2+1):
        left.append(y-d1+i)
    return left

def get_right_list(y,d1,d2):
    right = []
    for i in range(d2):
        right.append(y+i)
    for i in range(d1+1):
        right.append(y+d2-i)
    return right

INF = int(1e9)

answer = INF

for x in range(n):
    for y in range(n):
        for d1 in range(n):
            if d1 > y:
                break
            for d2 in range(n):
                if y + d2 >= n or x + d1 + d2 >= n:
                    break
                left = get_left_list(y,d1,d2)
                right = get_right_list(y,d1,d2)
                height = d1+d2+1
                visited = [[False]*n for _ in range(n)]
                max_population = get_fifth_area_poplutaion(city,visited,x,height,left,right)
                min_population = max_population
                x1 = [0,0,x+d1,x+d2+1]; y1 = [0,y+1,0,y-d1+d2]
                x2 = [x+d1,x+d2+1,n,n]; y2 = [y+1,n,y-d1+d2,n]
                for i in range(4):
                    population = get_population(city,visited,x1[i],y1[i],x2[i],y2[i])
                    max_population = max(max_population,population)
                    min_population = min(min_population,population)
                answer = min(answer,max_population-min_population)

print(answer)