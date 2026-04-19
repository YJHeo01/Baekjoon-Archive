from itertools import combinations
n,m,k = map(int,input().split())
answer = 0
array = [list(map(int,input().split())) for _ in range(n)]

ruby = []
for cnt in range(n):
    for j in range(m):
        ruby.append((array[cnt][j],cnt,j))

ruby.sort(reverse=True)

data = list(range(min(9,n*m)))

for cnt in range(1,k+1):
    test_case_list = list(combinations(data,cnt))
    for test_case in test_case_list:
        impossible = False
        tmp = 0
        for i in range(min(n*m,cnt)):
            value_i, x_i, y_i = ruby[test_case[i]]
            tmp += value_i
            for j in range(i):
                value_j, x_j, y_j = ruby[test_case[j]]
                if abs(x_i-x_j) + abs(y_i-y_j) == 1: impossible = True
        if impossible == False: answer = max(answer,tmp)

print(answer)