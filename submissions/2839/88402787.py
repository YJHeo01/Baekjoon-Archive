#질문게시판 질문 테스트용 제출
import sys

sys.setrecursionlimit(10**6)

n=int(input())
try_time = 0
memo = {}
def find_low(num, try_time):
    if num in memo:
        return memo[num]
    try_time += 1
    if (num -5) == 0 or (num -3) ==0:
        return try_time
    elif num -5 < 0:
        return 2000
    elif num -3 < 0:
        return 2000
    else:
        result = min(find_low(num-5,try_time), find_low(num-3,try_time)) 
    memo[num] = result
    return result           

result = find_low(n, try_time)

if result == 2000:
    print(-1)
    
else:
    print(result)