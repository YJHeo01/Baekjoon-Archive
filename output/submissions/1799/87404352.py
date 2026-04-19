from itertools import combinations
import sys

input = sys.stdin.readline

def main():
    down_right_dia = [[] for _ in range(2*n)] #좌측 상단에서 우측 하단으로 내려가는 대각선에 중복된 비숍 유무 체크
    up_left_dia = [False]*(2*n) #우측 상단에서 좌측 하단으로 내려가는 대각선에 중복된 비숍 유무 체크
    board = [list(map(int,input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:continue
            idx = i - j + n
            down_right_dia[idx].append((i,j))
    answer = 0
    for cnt in range(2*n-1,0,-1):
        for test_case in list(combinations(list(range(2*n)),cnt)):
            if backtracking(test_case,down_right_dia,up_left_dia,0):
                answer = cnt
                break
        if answer != 0: break
    print(answer)

def backtracking(test_case,down_right_dia,up_left_dia,idx):
    if idx == len(test_case): return True
    for x,y in down_right_dia[test_case[idx]]:
        if up_left_dia[x+y] == False:
            up_left_dia[x+y] = True
            if backtracking(test_case,down_right_dia,up_left_dia,idx+1) == True: return True
            up_left_dia[x+y] = False
    return False
    
def get_nx_ny(x,y):
    if y + 1 == n:
        return (x+1,0)
    else:
        return (x,y+1)

if __name__ == "__main__":
    n = int(input())
    main()