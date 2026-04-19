import sys

input = sys.stdin.readline

def main():
    n,m,k = map(int,input().split())
    friend_cnt = [1] * (n+1)
    candy_cnt = [-1] + list(map(int,input().split()))
    candy_cnt[0] = 0
    parent = list(range(n+1))
    for _ in range(m):
        a,b = map(int,input().split())
        union_parent(parent,a,b)
    for i in range(1,n+1):
        p_i = find_parent(parent,i)
        if p_i == i: continue
        friend_cnt[i] = 0
        friend_cnt[p_i] += 1
        candy_cnt[p_i] += candy_cnt[i]
    dp = [0] * k
    for i in range(1,n+1):
        if friend_cnt[i] == 0: continue
        for j in range(k-1,friend_cnt[i]-1,-1):
            if dp[j-friend_cnt[i]] < 0: continue
            dp[j] = max(dp[j-friend_cnt[i]]+candy_cnt[i],dp[j])
    print(max(dp))
    
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == "__main__":
    main()