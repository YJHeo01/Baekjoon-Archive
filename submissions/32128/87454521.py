import sys

input = sys.stdin.readline

def main():
    n,m,k = map(int,input().split())
    shuffle = [[0]]
    for _ in range(m):
        tmp = [[0]+list(map(int,input().split()))]
        for i in range(1,30):
            tmptmp = [0] * (n+1)
            for j in range(1,n+1):
                tmptmp[j] = tmp[i-1][tmp[i-1][j]]
            #print(tmptmp)
            tmp.append(tmptmp)
        shuffle.append(tmp)
    card = list(range(n+1))
    for _ in range(k):
        x,y = map(int,input().split())
        tmp = 1 << 29
        for i in range(29,-1,-1):
            if tmp & y:
                new_card = [0] * (n+1)
                for j in range(1,n+1):
                    new_card[shuffle[x][i][j]] = card[j]
                card = new_card
            tmp >>= 1
    print(*card[1:])
    

if __name__ == "__main__":
    main()