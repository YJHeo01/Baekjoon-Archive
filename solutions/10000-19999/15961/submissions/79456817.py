import sys

input = sys.stdin.readline

def main():
    n,d,k,c = map(int,input().split())
    cnt = [0] * (d+1)
    tmp = 0
    answer = 0
    array = []
    for _ in range(n):
        array.append(int(input()))
    for i in range(k):
        if cnt[array[i]] == 0:
            tmp += 1
        cnt[array[i]] += 1
    for right in range(k,n+k):
        left = (right - k)%n
        right %= n
        if cnt[array[right]] == 0: tmp += 1
        cnt[array[right]] += 1
        cnt[array[left]] -= 1
        if cnt[array[left]] == 0: tmp -= 1
        if cnt[c] == 0:
            answer = max(answer,tmp+1)
        else:
            answer = max(answer,tmp)
    print(answer)

if __name__ == "__main__":
    main()