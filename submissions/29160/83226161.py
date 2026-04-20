import sys

input = sys.stdin.readline

def main():
    n,k = map(int,input().split())
    array = [[] for _ in range(12)]
    sum_value = [0] * 12
    cnt = [0] * 12
    for _ in range(n):
        p,w = map(int,input().split())
        array[p].append(w)
        sum_value[p] += w
        cnt[p] += 1
    answer = 0
    for i in range(1,12):
        if array[i] == [] or sum_value[i] <= k:
            continue
        if cnt[i] == 1:
            answer += (array[i][0]-k)
            continue
        array[i].sort(reverse=True)
        tmp = k
        while True:
            if tmp == 0: break
            minus_value = min(tmp,array[i][0]-array[i][1]+1)
            tmp -= minus_value
            array[i][0] -= minus_value
            for j in range(1,cnt[i]):
                if array[i][j] <= array[i][j-1]: break
                array[i][j], array[i][j-1] = array[i][j-1],array[i][j]
        answer += array[i][0]
    print(answer)

if __name__ == "__main__":
    main()