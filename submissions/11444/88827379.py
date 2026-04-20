INF = 1000000007

n = int(input())

def cal(idx):
    if idx <= 0: return 0
    if idx <= 2: return 1
    if idx == 3: return 2
    if idx == 4: return 3
    if idx == 5: return 5
    if idx % 2 == 1: return (cal(idx//2) * cal(idx//2+2) + cal(idx//2-1) * cal(idx//2+1)) % INF
    else: return (cal(idx//2)*cal(idx//2+1)+cal(idx//2-1)*cal(idx//2)) % INF

answer = cal(n)

print(answer)