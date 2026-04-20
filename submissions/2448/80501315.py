import sys

sys.setrecursionlimit(10**6)

def main():
    star = [[' ']*(2*n) for _ in range(n)]
    solution(star,0,n-1,'C')
    answer = ''
    for i in range(n):
        for j in range(2*n):
            answer += star[i][j]
        answer += '\n'
    sys.stdout.write(answer)
def solution(star,row,column,star_type):
    if row % 6 == 0:
        star_column = [0]
    elif row % 6 == 1:
        star_column = [-1,1]
    elif row % 6 == 2:
        star_column = [-2,-1,0,1,2]
    elif row % 6 == 3:
        star_column = [3,-3]
    elif row % 6 == 4:
        star_column = [-4,-2,2,4]
    elif row % 6 == 5:
        star_column = [-5,-4,-3,-2,-1,1,2,3,4,5]
    for i in star_column:
        star[row][column+i] = '*'
    if row + 1 == n:
        return
    if row % 6 != 5:
        solution(star,row+1,column,star_type)
    else:
        if star_type == 'L':
            solution(star,row+1,column-6,'C')
        elif star_type == 'R':
            solution(star,row+1,column+6,'C')
        else:
            solution(star,row+1,column-6,'L')
            solution(star,row+1,column+6,'R')

if __name__ == "__main__":
    n = int(input())
    main()