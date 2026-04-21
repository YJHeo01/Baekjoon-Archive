import sys
input = sys.stdin.readline
n,k,q,m = map(int,input().split())
sleep = [False] * (n+3)
for i in list(map(int,input().split())): sleep[i] = True
attention = [False] * (n+3)

def check(attention,sleep,idx):
    if sleep[idx] == True: return
    for i in range(idx,n+3,idx):
        if sleep[i] == True: continue
        attention[i] = True

for i in list(map(int,input().split())):check(attention,sleep,i)

def get_prefix_sum(attention):
    prefix_sum = [0] * (n+3)
    for i in range(3,n+3):
        if attention[i] == False:
            prefix_sum[i] = prefix_sum[i-1] + 1
        else:
            prefix_sum[i] = prefix_sum[i-1]
    return prefix_sum

prefix_sum = get_prefix_sum(attention)

for _ in range(m):
    s,e = map(int,input().split())
    print(prefix_sum[e]-prefix_sum[s-1])