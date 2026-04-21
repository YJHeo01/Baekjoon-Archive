import sys

input = sys.stdin.readline

def main():
    t = int(input())
    for i in range(t):
        answer = solution()
        print("Case #"+str(i+1))
        print(answer)

def solution():
    ret_value = 0
    n,k = map(int,input().split())
    array = list(map(int,input().split()))
    left_idx = [-1] * 500001
    for idx in range(n):
        value = array[idx]
        for plus in range(k+1):
            if value + plus > 500000 or left_idx[value+plus] != -1:break
            left_idx[value+plus] = idx
        for plus in range(k,-1,-1):
            if value + plus > 500000 or left_idx[value+plus] != -1:break
            left_idx[value+plus] = idx
        ret_value += (idx - left_idx[value])
    return ret_value

if __name__ == "__main__":
    INF = int(1e9)
    main()