def main():
    n = int(input())
    w = int(input())
    position_a = [[1,1]]
    position_b = [[n,n]]
    for _ in range(w):
        tmp = list(map(int,input().split()))
        position_a.append(tmp)
        position_b.append(tmp)
    dp = [[INF]*(w+1) for _ in range(w+1)]
    dp[0][0] = 0
    for id in range(1,w+1):
        for i in range(id):
            dp[id][i] = min(dp[id][i],dp[id-1][i]+get_dist(position_a[id],position_a[id-1]))
            dp[i][id] = min(dp[i][id],dp[i][id-1]+get_dist(position_b[id],position_b[id-1]))
        for i in range(id):
            dp[id][id-1] = min(dp[id][id-1],dp[i][id-1]+get_dist(position_a[id],position_a[i]))
            dp[id-1][id] = min(dp[id-1][id],dp[id-1][i]+get_dist(position_b[id],position_b[i]))
    
    x,y = w,w
    for i in range(w):
        if dp[x][y] > dp[w][i]:
            x,y = i,w
        if dp[x][y] > dp[w][i]:
            x,y = w,i


    print(dp[x][y])
    answer = []

    while True:
        if x > y:
            answer.append(1)
            if x != y + 1:
                x -= 1
            else:
                for nx in range(y-1,-1,-1):
                    if dp[nx][y] + get_dist(position_a[x],position_a[nx]) == dp[x][y]:
                        x = nx
                        break

        else:
            answer.append(2)
            if y != x + 1:
                y -= 1
            else:
                for ny in range(x-1,-1,-1):
                    if dp[x][nx] + get_dist(position_b[y],position_b[nx]) == dp[x][y]:
                        y = ny
                        break
        
        if x == 0 or y == 0: break
    
    if y == 0:
        for _ in range(x):
            print(1)
    else:
        for _ in range(y):
            print(2)
    
    answer.reverse()
    for i in answer:
        print(i)
        
def get_dist(a,b):
    x_a, y_a = a
    x_b, y_b = b
    return abs(x_a-x_b) + abs(y_a-y_b)

if __name__ == "__main__":
    INF = int(1e9)
    main()