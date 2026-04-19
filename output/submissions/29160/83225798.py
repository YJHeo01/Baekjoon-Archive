import sys

input = sys.stdin.readline

def main():
    n,k = map(int,input().split())
    array = [[] for _ in range(12)]
    cnt = [0] * 12
    for _ in range(n):
        p,w = map(int,input().split())
        array[p].append(w)
        cnt[p] += 1
    for i in range(1,12):
        if array[i] == []:
            array[i].append(0)
        else:
            array[i].sort(reverse=True)
    for _ in range(k):
        for i in range(1,12):
            if array[i][0] == 0:
                continue
            array[i][0] -= 1
            for j in range(1,cnt[i]):
                if array[i][j] <= array[i][j-1]:
                    break
                array[i][j], array[i][j-1] = array[i][j-1],array[i][j]
    answer = 0
    for i in range(1,12):
        answer += array[i][0]
    print(answer)

if __name__ == "__main__":
    main()