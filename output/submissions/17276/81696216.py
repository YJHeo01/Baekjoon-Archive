import sys

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        global n
        n,d = map(int,input().split())
        array = get_array(n)
        d = d // 45
        d %= 8
        for _ in range(d):
            solution(array)
        for i in range(n):
            print(*array[i])

def get_array(n):
    array = []
    for _ in range(n):
        array.append(list(map(int,input().split())))
    return array

def solution(array):
    position = init_position()
    tmp = [[0]*n for _ in range(4)]
    for i in range(4):
        for j in range(n):
            tmp[i][j] = array[position[i][j][0]][position[i][j][1]]
    for i in range(3):
        for j in range(n):
            array[position[(i+1)][j][0]][position[(i+1)][j][1]] = tmp[i][j]
    for j in range(n):
        array[position[0][j][0]][position[0][j][1]] = tmp[3][n-1-j]

def init_position():
    position = [[[0]*2 for _ in range(n)] for _ in range(4)]
    for i in range(n):
        position[0][i][0] = i
        position[0][i][1] = n // 2
    for i in range(n):
        position[1][i][0] = i
        position[1][i][1] = n-1-i
    for i in range(n):
        position[2][i][0] = n // 2
        position[2][i][1] = n - 1 - i
    for i in range(n):
        position[3][i][0] = n - 1 - i
        position[3][i][1] = n - 1 - i
    return position

if __name__ == "__main__":
    main()