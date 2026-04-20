from itertools import combinations
import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    score = []
    for _ in range(n):
        score.append(list(map(int,input().split())))
    data = []
    for i in range(m):
        data.append(i)
    test_case = list(combinations(data,3))
    answer = 0
    for i,j,k in test_case:
        tmp = 0
        for x in range(n):
            tmp += max(score[x][i],score[x][j],score[x][k])
        answer = max(answer,tmp)
    print(answer)
                    
if __name__ == "__main__":
    main()