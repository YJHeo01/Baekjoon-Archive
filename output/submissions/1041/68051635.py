n = int(input())

dice = list(map(int,input().split()))

dice.sort()

if n == 1: print("15")
else:
    answer = dice[0] * (5 * n**2 - 8 * n + 4) 
    answer += dice[1] * ( 8*n - 8)
    answer += dice[2]*4

    print(answer)