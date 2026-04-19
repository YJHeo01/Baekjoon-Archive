n = int(input())

dice = list(map(int,input().split()))

INF = int(1e9)

answer = 250000000000000

if n == 1: print("15")
else:
    test_case_list = [(0,1,2),(0,1,3),(0,3,4),(0,2,4),(5,1,2),(5,1,3),(5,3,4),(5,2,4)]
    for test_case in test_case_list:
        a,b,c = test_case
        select_dice = [dice[a],dice[b],dice[c]]
        select_dice.sort()
        tmp = select_dice[0] * (5 * n**2 - 8 * n + 4) 
        tmp += select_dice[1] * ( 8*n - 8)
        tmp += select_dice[2]*4
        answer = min(answer,tmp)

    print(answer)