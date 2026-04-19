import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    bit_mask = []
    answer = m + 1
    for _ in range(m):
        array = list(map(int,input().split()))
        tmp = 0
        for i in array[1:]:
            tmp |= (1 << (i-1))
        bit_mask.append(tmp)
    complete_value = 2 ** n - 1
    for i in range(2**m):
        tmp = 0
        cnt = 0
        for j in range(m):
            if i & 1 << j == 0: continue
            tmp |= bit_mask[j]
            cnt += 1
        if cnt >= answer: continue
        if tmp == complete_value: answer = cnt
    
    if answer > m: answer = -1
    print(answer)

if __name__ == "__main__":
    main()