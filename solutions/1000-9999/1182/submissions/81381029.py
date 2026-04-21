from itertools import combinations

def main():
    n,s = map(int,input().split())
    array = list(map(int,input().split()))
    data = []
    answer = 0
    for i in range(n):
        data.append(i)
    for i in range(1,n+1):
        for test_case in list(combinations(data,i)):
            value = 0
            for idx in test_case:
                value += array[idx]
            if value == s:
                answer += 1
    print(answer)
                
if __name__ == "__main__":
    main()