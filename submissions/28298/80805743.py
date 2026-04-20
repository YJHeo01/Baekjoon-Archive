import sys

input = sys.stdin.readline

def main():
    solution(get_tile(n))

def get_tile(n):
    tile = []
    for _ in range(n):
        tile.append(list(input()))
    return tile

def solution(tile):
    alphabet_cnt = get_alphabet_cnt(tile)
    cnt = n*m
    answer_tile = []
    for i in range(k):
        tmp_answer_tile = []
        for j in range(k):
            tmp_cnt = 0
            tmp_alphabet = 'A'
            for l in range(26):
                if alphabet_cnt[i][j][l] > tmp_cnt:
                    tmp_cnt = alphabet_cnt[i][j][l]
                    tmp_alphabet = chr(ord('A')+l)
            tmp_answer_tile.append(tmp_alphabet)
            cnt -= tmp_cnt
        answer_tile.append(tmp_answer_tile)
    print(cnt)
    for i in range(n):
        for j in range(m):
            print(answer_tile[i%k][j%k],end="")
        print()

def get_alphabet_cnt(tile):
    alphabet_cnt = [[[0] * 26 for _ in range(k)] for _ in range(k)]
    for x in range(n):
        for y in range(m):
            alphabet_cnt[x%k][y%k][ord(tile[x][y])-ord('A')] += 1
    return alphabet_cnt

if __name__ == "__main__":
    n,m,k = map(int,input().split())
    main()