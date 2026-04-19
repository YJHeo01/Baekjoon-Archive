def main():
    x,y,w,h = map(int,input().split())
    answer = min(x,y,(w-x),(h-y))
    print(answer)

if __name__ == "__main__":
    main()