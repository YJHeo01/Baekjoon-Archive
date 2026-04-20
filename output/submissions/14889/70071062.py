INF = int(1e9)

n = int(input())
team_length = n // 2

def calculate_team_score(team):
    team_score = 0
    for i in team:
        for j in team:
            team_score += company[i][j]
    return team_score

def search_next_player(team):
    if team != []:
        return team[-1]
    else:
        return 0
    
def backtracking(start,link):
    start_length, link_length, ret_value = len(start),len(link),INF

    if start_length > team_length or link_length > team_length:
        return ret_value

    if team_length == start_length == link_length:
        start_sum = calculate_team_score(start)    
        link_sum = calculate_team_score(link)
        return abs(start_sum-link_sum)
    
    next_player = max(search_next_player(start),search_next_player(link)) + 1
    ret_value = min(ret_value,backtracking(start+[next_player],link))
    ret_value = min(ret_value,backtracking(start,link+[next_player]))
    return ret_value

company = [[0]*(n+1)]

for _ in range(n):
    company.append([0] + list(map(int,input().split())))

answer = min(backtracking([1],[]),backtracking([],[1]))

print(answer)
