import sys, heapq

input = sys.stdin.readline

def main():
    n,k = map(int,input().split())
    stone = [[False]*n for _ in range(n)]
    for _ in range(k):
        x,y = map(int,input().split())
        x -= 1; y -= 1
        stone[x][y] = True
    row_stone_cnt = [0] * n
    column_stone_cnt = [0] * n
    for row in range(n):
        for column in range(n):
            if stone[row][column] == True:
                row_stone_cnt[row] += 1
                column_stone_cnt[column] += 1
    q = []
    for i in range(n):
        if row_stone_cnt[i] != 0:
            heapq.heappush(q,(-row_stone_cnt[i],i))
        if column_stone_cnt[i] != 0:
            heapq.heappush(q,(-column_stone_cnt[i],i+n))
    answer = 0
    while q:
        cnt, idx = heapq.heappop(q)
        cnt *= -1
        if idx >= n:
            idx -= n
            if cnt != column_stone_cnt[idx]: continue
            for r in range(n):
                if stone[r][idx] == True:
                    stone[r][idx] = False
                    row_stone_cnt[r] -= 1
                    if row_stone_cnt[r] != 0: heapq.heappush(q,(-row_stone_cnt[r],r))
        else:
            if cnt != row_stone_cnt[idx]: continue
            for c in range(n):
                if stone[idx][c] == True:
                    stone[idx][c] = False
                    column_stone_cnt[c] -= 1
                    if column_stone_cnt[c] != 0: heapq.heappush(q,(-column_stone_cnt[c],c+n))
        answer += 1
    print(answer)

        
if __name__ == "__main__":
    main()