def main():
    L = list(map(int,input().split()))
    J = list(map(int,input().split()))
    print(backtracking(L,J,100,0,0))

def backtracking(L,J,hp,happy,start):
    ret_value = happy
    for i in range(start,n):
        if hp - L[i] > 0:
            ret_value = max(ret_value,backtracking(L,J,hp-L[i],happy+J[i],i+1))
    return ret_value

if __name__ == "__main__":
    n = int(input())
    main()