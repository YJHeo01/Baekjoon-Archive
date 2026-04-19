last_array = []

def main():
    array = sorted(list(map(int,input().split())))
    solution(array,[])

def solution(array,answer):
    if len(answer) == m:
        global last_array
        if answer not in last_array:
            last_array.append(answer)
            print(*answer)
        return
    for i in range(n):
        solution(array,answer + [array[i]])
    
if __name__ == "__main__":
    n,m = map(int,input().split())
    main()