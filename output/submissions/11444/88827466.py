import sys

INF = 1000000007

n = int(input())

def cal(table,idx):
    if idx in table: return table[idx] % INF
    if idx % 2 == 1:table[idx] = (cal(table,idx//2) * cal(table,idx//2+2) + cal(table,idx//2-1) * cal(table,idx//2+1)) % INF
    else: table[idx] = (cal(table,idx//2)*cal(table,idx//2+1)+cal(table,idx//2-1)*cal(table,idx//2)) % INF
    return table[idx]

table = dict([])
table[0] = 0
table[1] = 1
table[2] = 1

answer = cal(table,n)

print(answer)