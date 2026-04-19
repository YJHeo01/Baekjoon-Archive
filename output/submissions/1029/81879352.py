def main():
    array = []
    for _ in range(n):
        array.append(list(input()))
    print(solution(array,[False]*n,0,0,1))

def solution(array,visited,cost,vx,cnt):
    if cnt == n:
        print(cnt)
        exit(0)
    ret_value = cnt
    visited[vx] = True
    for nx in range(n):
        if visited[nx] == True: continue
        if int(array[vx][nx]) >= cost:
            ret_value = max(ret_value,solution(array,visited,int(array[vx][nx]),nx,cnt+1))
    visited[vx] = False
    return ret_value

if __name__ == "__main__":
    n = int(input())
    main()