import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p,q,a,b,c,d = map(int,input().split())
    bit = p
    coin = d * (q//d)
    answer = min(bit,coin)
    if bit > coin:
        left,right = 0, bit // a
        while left <= right:
            mid = (left+right) // 2
            cur_bit = bit - mid * a
            cur_coin = coin + mid * b
            answer = max(answer,min(cur_bit,cur_coin))
            if cur_bit > cur_coin:
                left = mid + 1
            else:
                right = mid - 1
    else:
        left, right = 0, coin // b
        while left <= right:
            mid = (left+right) // 2
            cur_bit = bit + mid * a
            cur_coin = coin - mid * b
            answer = max(answer,min(cur_bit,cur_coin))
            if cur_bit > cur_coin:
                right = mid - 1
            else:
                left = mid + 1
    print(answer)