def main():
    print(solution(input(),input()))

def solution(s,p):
    if p in s:
        return 1
    return 0

if __name__ == "__main__":
    main()