def main():
    n = int(input())
    s = list(input())
    
    array = [['']*n for _ in range(len(s)//n)]
    idx = 0
    
    for i in range(len(s)//n):
        if i % 2 == 0:
            start, end, change = 0,n,1
        else:
            start, end, change = n-1,-1,-1
        for j in range(start,end,change):
            array[i][j] = s[idx]
            idx += 1
    
    for j in range(n):
        for i in range(len(s)//n):
            print(array[i][j],end="")

if __name__ == "__main__":
    main()