def main():
    t = int(input())
    for _ in range(t):
        m,n = map(int,input().split())
        x,y = 0,0
        dx = [1,-1]
        i = 0
        print(1)
        for _ in range(n-1):
            print_answer(x,y)
            y += 1

        print_answer(x,y)
        for _ in range(m-1):
            x += dx[i]
            print_answer(x,y)
        y -= 1
        i += 1
        for _ in range(n-1):
            print_answer(x,y)
            for _ in range(m-2):
                x += dx[i]
                print_answer(x,y)
            i += 1; i %= 2
            y -= 1

def print_answer(x,y):
    print('('+str(x)+','+str(y)+')')

if __name__ == "__main__":
    main()