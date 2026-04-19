def main():
    n = int(input())
    array = list(map(int,input().split()))
    answer = 0
    for i in array:
        answer += min(n,i)
    print(answer)

if __name__ == "__main__":
    main()