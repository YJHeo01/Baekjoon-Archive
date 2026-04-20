def main():
    n,m = map(int,input().split())
    hate = [[False]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        hate[a][b], hate[b][a] = True, True
    answer = 0
    for i in range(3,n+1):
        for j in range(2,i):
            if hate[i][j] == True: continue
            for k in range(1,j):
                if hate[i][k] == False and hate[j][k] == False: answer += 1
    print(answer)
        
if __name__ == "__main__":
    main()