def main():
    tile = get_tile(n)
    cnt = 500 * 500
    target_point = [-1,-1]
    alphabet_cnt = [[[0] * 26 for _ in range(m)] for _ in range(n)]
    for x in range(0,n,k):
        for y in range(0,m,k):
            for dx in range(k):
                for dy in range(k):
                    alphabet_cnt[dx][dy][ord(tile[x+dx][y+dy])-ord('A')] += 1
 
    for x in range(0,n,k):
        for y in range(0,n,k):
            tmp = solution(tile,alphabet_cnt,(x,y))
            if cnt > tmp:
                cnt = tmp
                target_point = [x,y]
    print(cnt)
    for x in range(n):
        for y in range(m):
            print(tile[target_point[0]+x % k][target_point[1]+y % k],end="")
        print()
            
def get_tile(n):
    tile = []
    for _ in range(n):
        tile.append(list(input()))
    return tile

def solution(tile,alphabet_cnt,point):
    ret_value = n * m
    x, y = point
    for i in range(k):
        for j in range(k):
            ret_value -= alphabet_cnt[i][j][ord(tile[x+i][y+j])-ord('A')]
    return ret_value

if __name__ == "__main__":
    n,m,k = map(int,input().split())
    main()