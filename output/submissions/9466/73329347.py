t = int(input())

def solution(graph,visited,start):
    visited[start] = True
    idx = start
    while True:
        next_idx = graph[idx]
        if next_idx == start:
            return 0
        if visited[next_idx] == True:
            return 1
        visited[next_idx] = True
        idx = next_idx

for _ in range(t):
    n = int(input())
    student_list = [0] + list(map(int,input().split()))
    answer = 0
    for i in range(n,0,-1):
        visited = [False] * (n+1)
        answer += solution(student_list,visited,i)
    print(answer)