def main():
    n = int(input())
    num_list = list(map(int,input().split()))
    num_list.sort()
    answer = 1
    for i in range(n):
        if num_list[i] > answer: break
        answer += num_list[i]
    print(answer)

if __name__ == "__main__":
    main()