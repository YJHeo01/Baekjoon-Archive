def main():
    t = int(input())
    for _ in range(t):
        n,m = map(int,input().split())
        array = list(map(int,input().split()))
        print(solution(array,m,n))

def solution(array,target,n):
    important_cnt = [0] * 10
    for i in array: important_cnt[i] += 1
    idx, answer = 0,0
    for important in range(9,0,-1):
        if important_cnt[important] == 0: continue
        while True:
            if array[idx] == important:
                important_cnt[important] -= 1
                answer += 1
                if idx == target: return answer
            idx += 1
            idx %= n
            if important_cnt[important] == 0: break
    return answer

if __name__ == "__main__":
    main()