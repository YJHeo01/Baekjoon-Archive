def main():
    array = []
    for _ in range(n):
        array.append(list(input()))
    print(solution(array,[False]*n,0,0))

def solution(array,visited,cost,vx):
    ret_value = 0
    visited[vx] = True
    for nx in range(n):
        if visited[nx] == True: continue
        if int(array[vx][nx]) >= cost:
            ret_value = max(ret_value,solution(array,visited,int(array[vx][nx]),nx))
    visited[vx] = False
    ret_value += 1
    return ret_value

if __name__ == "__main__":
    n = int(input())
    main()