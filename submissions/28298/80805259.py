def main():
    tile = get_tile(n)
    cnt = int(1e9)
    target_point = [0,0]
    alphabet_cnt = [[[0] * 26 for _ in range(k)] for _ in range(k)]
    for x in range(n):
        for y in range(m):
            alphabet_cnt[x%k][y%k][ord(tile[x][y])-ord('A')] += 1
 
    for x in range(n-k+1):
        for y in range(m-k+1):
            tmp = solution(tile,alphabet_cnt,(x,y))
            if cnt > tmp:
                cnt = tmp
                target_point = [x,y]
    print(cnt)
    for x in range(n):
        for y in range(m):
            print(tile[target_point[0]+(x % k)][target_point[1]+(y % k)],end="")
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