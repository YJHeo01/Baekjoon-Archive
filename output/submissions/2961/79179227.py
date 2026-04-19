def main():
    array = []
    for _ in range(n):
        array.append(list(map(int,input().split())))
    answer = int(1e9)
    for i in range(n):
        answer = min(answer,solution(array,i,array[i][0],array[i][1]))
    print(answer)

def solution(array,idx,s,b):
    ret_value = abs(s-b)
    for next_idx in range(idx+1,n):
        ret_value = min(ret_value,solution(array,next_idx,s*array[next_idx][0],b+array[next_idx][1]))
    return ret_value

if __name__ == "__main__":
    n = int(input())
    main()