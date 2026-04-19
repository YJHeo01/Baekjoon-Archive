def main():
    solution('',0,0,0)
    print(-1)

def solution(s,B_cnt,i_j_cnt,length):
    if i_j_cnt == k:
        for c in s:print(c,end="")
        for _ in range(n-len(s)): print('A',end="")
        exit(0)
    if length == n: return
    solution('B'+s,B_cnt+1,i_j_cnt,length+1)
    if i_j_cnt + B_cnt <= k:
        solution('A'+s,B_cnt,i_j_cnt+B_cnt,length+1)
    
if __name__ == "__main__":
    n,k = map(int,input().split())
    main()
