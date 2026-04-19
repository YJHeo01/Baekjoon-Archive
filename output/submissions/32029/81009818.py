#2024 UCPC 예선(팀명 본선 다익스트라 제출 코드)
#https://ucpc.acmicpc.net/source/80971096

import sys

input = sys.stdin.readline


def main():
    n,a,b = map(int,input().split())
    array = list(map(int,input().split()))
    array.sort()
    answer = 0
    for x in range(a):    
        for i in range(n):
            cnt = 0
            time = a
            for j in range(i):
                if time <= array[j]:
                    cnt += 1
                    time += a
            time += b * x
            time -= x
            for j in range(i,n):
                if time <= array[j]:
                    cnt += 1
                    time += (a-x)
            answer = max(answer,cnt)
    print(answer)

if __name__ == "__main__":
    main()