def main():
    array = list(map(int,input().split()))
    array.sort()
    backtracking(array,[False]*n,[])

def backtracking(array,visited,answer):
    if len(answer) == m:
        print(*answer)
        return
    last_value = -1
    for i in range(n):
        if visited[i] == True or last_value == array[i]: continue
        last_value = array[i]
        visited[i] = True
        backtracking(array,visited,answer+[array[i]])
        visited[i] = False
    return

if __name__  == "__main__":
    n,m = map(int,input().split())
    main()