def main():
    n = int(input())
    house = list(map(int,input().split()))
    time = list(map(int,input().split()))
    answer = 0
    for i in range(n):
        answer = max(answer,max(house[i],time[i])+house[i])
    print(answer)

if __name__ == "__main__":
    main()