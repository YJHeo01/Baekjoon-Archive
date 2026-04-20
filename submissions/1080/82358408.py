def main():
    a = [list(input()) for _ in range(n)]
    b = [list(input()) for _ in range(n)]
    answer = 0
    for x in range(n-2):
        for y in range(m-2):
            if a[x][y] != b[x][y]:
                reverse_matrix(a,(x,y))
                answer += 1
    answer = min(compare_matrix(a,b),answer)
    print(answer)

def reverse_matrix(matrix,point):
    x,y = point
    for dx in range(3):
        for dy in range(3):
            nx,ny = x + dx, y + dy
            if matrix[nx][ny] == '1':
                matrix[nx][ny] = '0'
            else:
                matrix[nx][ny] = '1'

def compare_matrix(a,b):
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return -1
    return n*m+1

if __name__ == "__main__":
    n,m = map(int,input().split())   
    main()