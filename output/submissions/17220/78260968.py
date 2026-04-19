import sys

input = sys.stdin.readline
A_ascii = ord('A')

def main():
    global n,m
    n,m = map(int,input().split())
    graph, arrest, start = set_init()
    input_grpah(graph,start)
    input_arrest(arrest)
    answer = 0
    for i in range(n):
        c = chr(A_ascii + i)
        if start[c] == False or arrest[c] == True and graph[c] == []: continue
        answer += (dfs(graph,arrest,c)-1)
    print(answer)
    
def set_init():
    graph, arrest, start = {}, {}, {}
    for i in range(n):
        c = chr(A_ascii + i)
        graph[c] = []; arrest[c] = False; start[c] = True
    return graph,arrest,start

def input_grpah(graph,start):
    for _ in range(m):
        a,b = input().split()
        graph[a].append(b)
        start[b] = False

def input_arrest(arrest):
    information = list(input().split())
    if information[0] == '0': return
    for c in information[1:]: arrest[c] = True

def dfs(graph,arrest,start):
    ret_value = 1
    for nx in graph[start]:
        if arrest[nx] == True: continue
        ret_value += dfs(graph,arrest,nx)
    return ret_value

if __name__ == "__main__":
    main()