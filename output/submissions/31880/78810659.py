import sys

sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
lucky_A = list(map(int,input().split()))
lucky_B = list(map(int,input().split()))
visited_A = [False]*n
visited_B = [False]*m


def solution(visited_A,visited_B,score):
    ret_value = score
    if score != 0:
        for i in range(m):
            if visited_B[i] == False:
                visited_B[i] = True
                ret_value = max(ret_value,solution(visited_A,visited_B,score*lucky_B[i]))
                visited_B[i] = False
    for i in range(n):
        if visited_A[i] == False:
            visited_A[i] = True
            ret_value = max(ret_value,solution(visited_A,visited_B,score+lucky_A[i]))
            visited_A[i] = False
    return ret_value

answer = solution(visited_A,visited_B,0)

print(answer)