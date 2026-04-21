t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int,input().split()))
    answer = -1
    left_two_cnt = 0; right_two_cnt = 0
    for i in range(n):
        if array[i] == 2: right_two_cnt += 1
    for i in range(n):
        if array[i] == 2:
            left_two_cnt += 1
            right_two_cnt -= 1
        if left_two_cnt == right_two_cnt:
            answer = i + 1
            break
    print(answer)