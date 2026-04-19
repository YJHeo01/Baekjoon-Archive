import sys

input = sys.stdin.readline

n,m = map(int,input().split())

point = 0

game_board = [0] * (n)

for i in range(n):
    game_board[i] = int(input())

answer = m

for i in range(1,m+1):
    point += int(input())
    if point >= n:
        answer = i
        break
    point += game_board[point]
    if point >= n:
        answer = i
        break

print(answer)