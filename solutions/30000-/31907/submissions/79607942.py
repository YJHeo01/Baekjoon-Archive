def main():
    n = int(input())
    picture = [['.']*(4*n) for _ in range(3*n)]
    for i in range(n):
        for j in range(n):
            picture[i][j] = 'G'
    for i in range(n,2*n):
        for j in range(n,2*n):
            picture[i][j] = 'I'
    for i in range(n,2*n):
        for j in range(3*n,4*n):
            picture[i][j] = 'T'
    for i in range(2*n,3*n):
        for j in range(2*n,3*n):
            picture[i][j] = 'S'
    
    for i in range(3*n):
        for j in range(4*n):
            print(picture[i][j],end="")
        print()

if __name__  == "__main__":
    main()