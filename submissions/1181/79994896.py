def main():
    n = int(input())
    answer = [[] for _ in range(51)]
    for _ in range(n):
        tmp = input()
        length = len(tmp)
        answer[length].append(tmp)
    for i in range(1,51):
        if answer[i] == []: continue
        answer[i].sort()
        length = len(answer[i])
        for j in range(length):
            if j > 0 and answer[i][j] == answer[i][j-1]:continue
            print(answer[i][j])

if __name__ == "__main__":
    main()