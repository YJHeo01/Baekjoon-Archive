from collections import deque

def main():
    start = list(map(int,input().split()))
    start.sort()
    answer = solution(start)
    print(answer)

def solution(start):
    a,b,c = start
    if a== b and b == c: return 1
    queue = deque([start])
    visited = [[[False]*1501 for _ in range(501)]for _ in range(501)]
    visited[a][b][c] = True
    command_list = [[0,2,1],[0,1,2],[1,2,0]]
    while queue:
        stone_list = queue.popleft()
        for x,y,z in command_list:
            if stone_list[x] == stone_list[y]: continue
            na = stone_list[y] - stone_list[x]
            nb = stone_list[x] + stone_list[x]
            nc = stone_list[z]
            if na == nb and nb == nc: return 1
            next_stone_list = [na,nb,nc]
            next_stone_list.sort()
            if visited[next_stone_list[0]][next_stone_list[1]][next_stone_list[2]] == True: continue
            visited[next_stone_list[0]][next_stone_list[1]][next_stone_list[2]] = True
            queue.append(next_stone_list)
    return 0

if __name__ == "__main__":
    main()