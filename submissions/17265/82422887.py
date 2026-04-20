def main():
    array = [list(input().split()) for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if (x+y) % 2 != 0:
                continue
            array[x][y] = int(array[x][y])
    print(max_value(array,(0,0),array[0][0]),min_value(array,(0,0),array[0][0]))

def max_value(array,position,cur_value):
    x,y = position
    if x >= n or y >= n:
        return -INF
    if x == n - 1 and y == n - 1:
        return cur_value
    if type(array[x][y]) == int:
        return max(max_value(array,(x+1,y),cur_value),max_value(array,(x,y+1),cur_value))
    dx = [0,1]
    dy = [1,0]
    ret_value = -INF
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= n or ny >= n:
            continue
        ret_value = max(ret_value,max_value(array,(nx,ny),next_value(cur_value,array[x][y],array[nx][ny])))
    return ret_value

def min_value(array,position,cur_value):
    x,y = position
    if x >= n or y >= n:
        return INF
    if x == n - 1 and y == n - 1:
        return cur_value
    if type(array[x][y]) == int:
        return min(min_value(array,(x+1,y),cur_value),min_value(array,(x,y+1),cur_value))
    dx = [0,1]
    dy = [1,0]
    ret_value = INF
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= n or ny >= n:
            continue
        ret_value = min(ret_value,min_value(array,(nx,ny),next_value(cur_value,array[x][y],array[nx][ny])))
    return ret_value

def next_value(value_a,oper,value_b):
    if oper == '+':
        return value_a + value_b
    if oper == '-':
        return value_a - value_b
    return value_a * value_b

if __name__ == "__main__":
    n = int(input())
    INF = int(1e9)
    main()