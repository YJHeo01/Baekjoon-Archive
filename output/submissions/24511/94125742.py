n = int(input())

a = list(map(int,input().split()))

b = list(map(int,input().split()))

m = int(input())

c = list(map(int,input().split()))

queue_stack = []

for i in range(n):
    queue_stack.append(deque([b[i]]))

answer = []

for i in range(n):
    a_i = a.pop()
    b_i = b.pop()
    if a_i == 0:
        answer.append(b_i)

answer += c

print(*answer[:m])