import sys

input = sys.stdin.readline

def main():
    n = int(input())
    card = []
    for _ in range(n):
        card.append(list(map(int,input().split())))
    answer = 0
    max_score = 0
    for num in range(n):
        score = 0
        for i in range(2,5):
            for j in range(1,i):
                for k in range(j):
                    score = max(score,(card[num][i]+card[num][j]+card[num][k])%10)
        if score >= max_score:
            answer = num+1
            max_score = score
    print(answer)

if __name__ == "__main__":
    main()