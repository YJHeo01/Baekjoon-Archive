from collections import deque

visited = [[False]* 1000000 for _ in range(11)]

n, k = map(int,input().split())

n = list(str(n))

l = len(n)

def get_next_value(value):
    next_value = 0
    for i in range(l):
        next_value *= 10
        next_value += int(value[i])
    return next_value

def solution(visited,start):
    answer = -1
    queue = deque([[start,1]])
    while queue:
        value,move_cnt = queue.popleft()
        for i in range(l):
            for j in range(i+1,l):
                value[i], value[j] = value[j], value[i]
                next_value = get_next_value(value)
                if visited[move_cnt][next_value] == True or value[0] == '0':
                    value[i], value[j] = value[j], value[i]
                    continue
                visited[move_cnt][next_value] = True
                next_value = list(str(next_value))               
                if move_cnt == k:
                    next_value = get_next_value(next_value)
                    answer = max(answer,next_value)
                else:                
                    queue.append((next_value,move_cnt+1))
                value[i], value[j] = value[j], value[i]
    return answer

answer = solution(visited,n)

print(answer)
