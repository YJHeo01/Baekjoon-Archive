def main():
    a,b,d,n = map(int,input().split())
    bug = [0] * d
    answer, bug[0] = 1,1
    new_bug = 0
    for _ in range(n):
        answer -= bug[d-1]
        for i in range(d-1,0,-1):
            bug[i] = bug[i-1]
        new_bug += bug[a]
        new_bug -= bug[b]
        bug[0] = new_bug
        answer += new_bug
        answer %= 1000
    print(answer)

if __name__ == "__main__":
    main()