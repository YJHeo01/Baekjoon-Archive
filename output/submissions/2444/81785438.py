def main():
    n = int(input())
    star = [[' ']*(2*n-1) for _ in range(2*n-1)]
    vy = n-1
    for vx in range(n):
        for dy in range(vx+1):
            star[vx][vy+dy] = '*'
            star[vx][vy-dy] = '*'
            star[2*n-2-vx][vy+dy] = '*'
            star[2*n-2-vx][vy-dy] = '*'
    for row in star:
        for i in row:
            print(i,end="")
        print()

if __name__ == "__main__":
    main()