import sys

input = sys.stdin.readline

def main():
    n = int(input())
    finish = [False] * (n+1)
    friend = [[False]*(n+1) for _ in range(n+1)]
    while True:
        a,b = map(int,input().split())
        if a == -1 and b == -1: break
        friend[a][b], friend[b][a] = True, True
    last_idx = 0
    A_team, B_team = [], []
    while True:
        first_idx = -1
        for i in range(last_idx+1,n+1):
            if finish[i] == False:
                first_idx = i
                break
        if first_idx == -1: break
        tmp_A_team, tmp_B_team = [],[]
        tmp_A_team.append(first_idx)
        finish[first_idx] = True
        for i in range(first_idx+1,n+1):
            if friend[first_idx][i] == False: tmp_B_team.append(i)
        for i in tmp_B_team:
            finish[i] = True
            for j in tmp_B_team:
                if i == j: continue
                if friend[i][j] == False:
                    print(-1)
                    exit(0)
        for i in range(first_idx+1,n+1):
            if finish[i]: continue
            possible_A_team = check_possible_team(friend,tmp_A_team,i)
            possible_B_team = check_possible_team(friend,tmp_B_team,i)
            if possible_A_team and possible_B_team: continue
            if possible_A_team:
                tmp_A_team.append(i)
            elif possible_B_team:
                tmp_B_team.append(i)
            else:
                print(-1)
                exit(0)
            finish[i] = True
        A_team += tmp_A_team
        B_team += tmp_B_team
        last_idx = first_idx
    A_team.sort(); B_team.sort()
    print(1)
    for i in A_team:
        print(i,end=" ")
    print(-1)
    for i in B_team:
        print(i,end=" ")
    print(-1)

def check_possible_team(friend,team,idx):
    for i in team:
        if friend[i][idx] == False: return False
    return True
    
if __name__ == "__main__":
    main()