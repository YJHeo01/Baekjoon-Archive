INF = 21

def main():
    paper = get_paper()
    dp = get_dp(paper)
    answer = solution(dp,[5,5,5,5,5],(0,0))
    if answer >= 21: answer = -1
    print(answer)

def get_paper():
    paper = []
    for _ in range(10): paper.append(list(map(int,input().split())))
    return paper

def get_dp(paper):
    dp = [[0]*10 for _ in range(10)]
    for i in range(10): dp[i][9] = paper[i][9]; dp[9][i] = paper[9][i]
    for x in range(8,-1,-1):
        for y in range(8,-1,-1):
            if paper[x][y] == 0: continue
            dp[x][y] = min(dp[x+1][y],dp[x][y+1],dp[x+1][y+1]) + 1
    return dp

def solution(dp,paper_list,point):
    x,y = point
    if x == 10: return 25 - sum(paper_list)
    ret_value = INF
    if dp[x][y] == 0: 
        next_point = get_next_point(x,y)
        return solution(dp,paper_list,next_point)
    size = min(dp[x][y],5)
    for i in range(size):
        if paper_list[i] == 0: continue
        paper_list[i] -= 1
        length = i + 1
        attach_paper_list = attach_paper(dp,point,length)
        next_point = get_next_point(x,y+i)
        ret_value = min(ret_value,solution(dp,paper_list,next_point))
        clear_paper(dp,attach_paper_list)
        paper_list[i] += 1
    return ret_value

def attach_paper(dp,start,length):
    x,y = start
    ret_value = []
    for i in range(length):
        for j in range(length):
            ret_value.append([x+i,y+j,dp[x+i][y+j]])
            dp[x+i][y+j] = 0
    return ret_value

def clear_paper(dp,attach_paper_list):
    for x,y,value in attach_paper_list: dp[x][y] = value

def get_next_point(x,y):
    if y >= 9: return (x+1,0)
    return (x,y+1)

if __name__ == "__main__":
    main()