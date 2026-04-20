import sys

input = sys.stdin.readline

def main():
    space = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
    for _ in range(int(input())):
        a,b,c,d = map(int,input().split())
        answer = 'NO'
        for i in range(3):
            if space[a][i] == space[b][i] and space[b][i] == space[c][i] and space[c][i] == space[d][i]:
                answer = 'YES'
        print(answer)

if __name__ == "__main__":
    main()