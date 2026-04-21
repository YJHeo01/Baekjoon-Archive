n,k,p,x = input().split()


adj_matrix = [
[0, 4, 3, 3, 4, 3, 2, 3, 1, 2]
,[4, 0, 5, 3, 2, 5, 6, 1, 5, 4]
,[3, 5, 0, 2, 5, 4, 3, 4, 2, 3]
,[3, 3, 2, 0, 3, 2, 3, 2, 2, 1]
,[4, 2, 5, 3, 0, 3, 4, 3, 3, 2]
,[3, 5, 4, 2, 3, 0, 1, 4, 2, 1]
,[2, 6, 3, 3, 4, 1, 0, 5, 1, 2]
,[3, 1, 4, 2, 3, 4, 5, 0, 4, 3]
,[1, 5, 2, 2, 3, 2, 1, 4, 0, 1]
,[2, 4, 3, 1, 2, 1, 2, 3, 1, 0]
]
n = int(n)
p = int(p)
k = int(k)
x = list(str(x))
x = ['0'] * (k-len(x)) + x
max_stair = 10 ** k 

answer = 0

for i in range(1,n+1):
    stack = list(str(i))
    stack = ['0'] * (k-len(stack)) + stack
    idx = k
    tmp = 0
    while stack:
        idx -= 1
        num = stack.pop()
        tmp += adj_matrix[int(x[idx])][int(num)]
    if tmp <= p:
        print(i)
        answer += 1
answer -= 1
print(answer)