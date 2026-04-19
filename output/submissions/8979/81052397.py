import sys

input = sys.stdin.readline

def main():
    n,k = map(int,input().split())
    country = [[0]*3 for _ in range(n+1)]
    for _ in range(n):
        idx, gold, silver, bronze = map(int,input().split())
        country[idx] = [gold,silver,bronze]
    answer = 1
    for i in range(1,n+1):
        if country[i][0] > country[k][0]:
            answer += 1
        elif country[i][0] == country[k][0]:
            if country[i][1] > country[k][1] or (country[i][1] == country[k][1] and country[i][2] > country[k][2]):
                answer += 1
    print(answer)

if __name__ == "__main__":
    main()