def main():
    array = list(map(int,input().split()))
    array.sort()
    backtracking(array,[],0)
    
def backtracking(array,answer,length):
    if length == m:
        for i in answer:
            print(i,end=" ")
        print()
        return
    for i in range(n):
        backtracking(array,answer + [array[i]],length+1)

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()