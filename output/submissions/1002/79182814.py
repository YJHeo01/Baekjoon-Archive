def main():
    t = int(input())
    for _ in range(t):
        answer = 0
        x1,y1,r1,x2,y2,r2 = map(int,input().split())
        mutiple_dx = [-1,1,1]
        mutiple_dy = [-1,-1,1]
        for dx in range(r1):
            dy = r1 - dx
            for i in range(3):
                nx = x1 + dx * mutiple_dx[i]
                ny = y1 + dy * mutiple_dy[i]
                if abs(x2-nx) + abs(y2-ny) == r2:
                    answer += 1
        print(answer)
            
if __name__ == "__main__":
    main()