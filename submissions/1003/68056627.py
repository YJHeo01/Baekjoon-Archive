T = int(input())
n = [0]*T
for i in range(T):
    n[i] = int(input())
n_max = max(n)
d = [[0] * 2 for _ in range(n_max+1)]
d[0] = [1,0]
if n_max >= 1:
    d[1] = [0,1]
    for i in range(2,n_max+1):
        d[i][0] = d[i-2][0] + d[i-1][0]
        d[i][1] = d[i-2][1] + d[i-1][1]

for i in n:
    print(d[i][0], d[i][1])