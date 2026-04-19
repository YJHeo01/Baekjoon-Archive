from itertools import combinations
import sys

input = sys.stdin.readline

def main():
    graph = get_graph()
    A_team_candidate = get_A_team_candidate(graph)
    A_team_candidate_cnt = len(A_team_candidate)
    possible = False
    for i in range(A_team_candidate_cnt+1):
        test_case_list = list(combinations(A_team_candidate,i))
        for A_team in test_case_list:
            A_team = [1] + list(A_team)
            B_team = get_B_team(A_team)
            if check_correct_team(graph,A_team) and check_correct_team(graph,B_team):
                print_team(A_team)
                print_team(B_team)
                break
        if possible == True:
            break

def get_graph():
    graph = [[] for _ in range(n+1)]
    while True:
        a,b = map(int,input().split())
        if a == -1:
            break
        graph[a].append(b)
        graph[b].append(a)
    return graph

def get_A_team_candidate(graph):
    ret_value = []
    for candidate in graph[1]:
        ret_value.append(candidate)
    return ret_value

def get_B_team(A_team):
    B_team = []
    for i in range(1,n+1):
        if i in A_team:
            continue
        B_team.append(i)
    return B_team

def check_correct_team(graph,team):
    for idx in team:
        friend = get_friend(graph,idx)
        for member in team:
            if friend[member] == False:
                return False
    return True

def get_friend(graph,idx):
    friend = [False] * (n+1)
    friend[idx] = True
    for nx in graph[idx]:
        friend[nx] = True
    return friend

def print_team(team):
    for idx in team:
        print(idx,end=" ")
    print(-1)

if __name__ == "__main__":
    n = int(input())
    main()