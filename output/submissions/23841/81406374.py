def main():
    n,m = map(int,input().split())
    picture = []
    for _ in range(n):
        picture.append(list(input()))
    for i in range(n):
        for j in range(m//2):
            if picture[i][j] != '.':
                picture[i][m-1-j] = picture[i][j]
            elif picture[i][m-1-j] != '.':
                picture[i][j] = picture[i][m-1-j]
    for i in range(n):
        for j in range(m):
            print(picture[i][j],end="")
        print()

if __name__ == "__main__":
    main()