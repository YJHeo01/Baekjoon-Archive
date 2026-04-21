def main():
    x,y = map(int,input().split())
    if x < y: x,y = y,x
    answer = x + y + y // 10
    print(answer)

if __name__ == "__main__":
    main()