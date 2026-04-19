import sys

input = sys.stdin.readline

def main():
    parent = init_parent()
    while True:
        a,b = map(int,input().split())
        if a == -1:
            break
        union_parent(parent,a,b)
    captain_member_list = get_captain_member_list(parent)
    min_team_cnt = len(captain_member_list)
    if min_team_cnt >= 3:
        print(-1)
        return
    print(1)
    A_team = []; B_team = []
    if min_team_cnt == 1:
        for i in range(1,n+1):
            if i % 2 == 1:
                A_team.append(i)
            else:
                B_team.append(i)
    else:
        for i in range(1,n+1):
            if find_parent(parent,i) == 1:
                A_team.append(i)
            else:
                B_team.append(i)
    print_team_member(A_team)
    print_team_member(B_team)

def init_parent():
    parent = [0] * (n+1)
    for i in range(n+1):
        parent[i] = i
    return parent

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def get_captain_member_list(parent):
    captain_member_list = []
    for i in range(1,n+1):
        idx = find_parent(parent,i)
        if idx not in captain_member_list:
            captain_member_list.append(idx)
    return captain_member_list

def print_team_member(team):
    for i in team:
        print(i,end=" ")
    print(-1)

if __name__ == "__main__":
    n = int(input())
    main()