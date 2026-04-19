def main():
    a,b,d,n = map(int,input().split())
    bug = [0] * (n+1)
    bug[0] = 1
    new_bug = 0
    for i in range(a,b):
        new_bug += bug[i-a]
        bug[i] = new_bug % 1000
    for i in range(b,n+1):
        new_bug += bug[i-a]
        new_bug -= bug[i-b]
        if new_bug < 0: new_bug = 0
        bug[i] = new_bug % 1000
    answer = 0
    for i in range(d):
        answer += bug[n-i]
    answer %= 1000
    print(answer)

if __name__ == "__main__":
    main()