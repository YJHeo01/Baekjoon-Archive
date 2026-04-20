def main():
    array = init_array()
    command = list(map(int,input().split()))
    for c in command:
        array = control_array(array,c)
    print_array(array)

def init_array():
    array = []
    for _ in range(n):
        array.append(list(map(int,input().split())))
    return array

def control_array(array,c):
    if c == 1:
        array = one(array)
    elif c == 2:
        array = two(array)
    elif c == 3:
        array = three(array)
    elif c == 4:
        array = four(array)
    elif c == 5:
        array = five(array)
    else:
        array = six(array)
    return array

def one(array):
    length = n // 2
    for i in range(length):
        for j in range(m):
            array[i][j], array[n-1-i][j]  = array[n-1-i][j], array[i][j]
    return array

def two(array):
    length = m // 2
    for i in range(n):
        for j in range(length):
            array[i][j], array[i][m-1-j] = array[i][m-1-j], array[i][j]
    return array

def three(array):
    global m,n
    m,n = n,m
    new_array = [[0]*m for _ in range(n)]
    for x in range(m):
        for y in range(n):
            nx = y
            ny = m - 1 - x
            new_array[nx][ny] = array[x][y] 
    return new_array

def four(array):
    global m,n
    m,n = n,m
    new_array = [[0]*m for _ in range(n)]
    for x in range(m):
        for y in range(n):
            nx = n - 1 - y
            ny = x
            new_array[nx][ny] = array[x][y]
    return new_array

def five(array):
    new_array = [[0]*m for _ in range(n)]
    x1, y1, x2, y2 = 0, 0, n // 2, m // 2
    new_array = five_six(new_array,array,(x1,y1),(x1,y2))
    new_array = five_six(new_array,array,(x1,y2),(x2,y2))
    new_array = five_six(new_array,array,(x2,y2),(x2,y1))
    new_array = five_six(new_array,array,(x2,y1),(x1,y1))
    return new_array

def six(array):
    new_array = [[0]*m for _ in range(n)]
    x1, y1, x2, y2 = 0, 0, n // 2, m // 2
    new_array = five_six(new_array,array,(x1,y2),(x1,y1))
    new_array = five_six(new_array,array,(x2,y2),(x1,y2))
    new_array = five_six(new_array,array,(x2,y1),(x2,y2))
    new_array = five_six(new_array,array,(x1,y1),(x2,y1))
    return new_array

def five_six(new_array,array,cur_start,new_start):
    new_x, new_y = new_start
    cur_x, cur_y = cur_start
    r = n // 2; c = m // 2
    for i in range(r):
        for j in range(c):
            new_array[new_x+i][new_y+j] = array[cur_x+i][cur_y+j]
    return new_array

def print_array(array):
    for i in range(n):
        for j in range(m):
            print(array[i][j],end=" ")
        print()

if __name__ == "__main__":
    n,m,r = map(int,input().split())
    main()