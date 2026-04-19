def main():
    visited = [[False]*(k+1) for _ in range(n+1)]
    visited[0][0] = True
    solution('',visited,0,0,0)
    print(-1)

def solution(s,visited,B_cnt,i_j_cnt,length):
    if i_j_cnt == k:
        for c in s:print(c,end="")
        for _ in range(n-len(s)): print('A',end="")
        exit(0)
    if length == n: return
    if visited[B_cnt+1][i_j_cnt] == False:
        visited[B_cnt+1][i_j_cnt] = False
        solution('B'+s,visited,B_cnt+1,i_j_cnt,length+1)
    if i_j_cnt + B_cnt <= k and visited[B_cnt][i_j_cnt+B_cnt] == False:
        visited[B_cnt][i_j_cnt+B_cnt] = True
        solution('A'+s,visited,B_cnt,i_j_cnt+B_cnt,length+1)
    
if __name__ == "__main__":
    n,k = map(int,input().split())
    main()
