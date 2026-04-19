def main():
    n = int(input())
    visited = [False] * (n+1)
    solution([],visited,n)

def solution(array,visited,n):
    if len(array) == n:
        print(*array)
        return
    for i in range(1,n+1):
        if visited[i] == False:
            visited[i] = True
            solution(array+[i],visited,n)
            visited[i] = False

if __name__ == "__main__":
    main()