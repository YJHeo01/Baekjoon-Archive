import sys
sys.setrecursionlimit(10**6)

t = int(input())

test_case = []
start_student = 0


def matching_team(team,new_member):
    global visited,answer
    if team != []:
        if new_member == team[0]:
            for member in team:
                if visited[member] == False:
                    visited[member] = True
                    answer -= 1
            return
        elif visited[new_member] == True:
            return
        elif new_member == test_case[new_member]:
            if visited[new_member] == False:
                visited[new_member] = True
                answer -= 1
            return
    matching_team(team + [new_member],test_case[new_member])
    return
for _ in range(t):
    n = int(input())
    answer = n
    test_case = [0] + list(map(int,input().split()))
    visited = [False] * (n+1)
    for i in range(1,n+1):
        matching_team([],i)
    print(answer)