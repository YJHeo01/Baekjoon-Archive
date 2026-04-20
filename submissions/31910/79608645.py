def main():
    array = []
    for _ in range(n):
        array.append(list(map(int,input().split())))
    answer = solution(array,array[0][0],(0,0))
    print(answer)

def solution(array,value,position):
    x,y = position
    if x == n-1 and y == n-1:
        return value
    ret_value = 0
    dx = [1,0]
    dy = [0,1]
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= n or ny >= n: continue
        ret_value = max(ret_value,solution(array,value*2+array[nx][ny],(nx,ny)))
    return ret_value

if __name__  == "__main__":
    n = int(input())
    main()