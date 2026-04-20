n = int(input())

m = int(input())

edges = []

for _ in range(m):
    cur_node, next_node, percent = input().split()
    edges.append([ord(cur_node)-ord('A'),ord(next_node)-ord('A'),float(percent)])

exist = [[0]*4 for _ in range(n+1)]

for i in range(4):
    exist[0][i] = 25

for i in range(n):
    for cur_node, next_node, percent in edges:
        exist[i+1][next_node] += exist[i][cur_node] * percent

for answer in exist[n]:
    print(answer)