import sys

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        answer = solution()
        print(answer)

def solution():
    n = int(input())
    number_list = [[]for _ in range(11)]
    check_number = [{} for _ in range(11)]
    for _ in range(n):
        tmp = input().rstrip()
        number_list[len(tmp)].append(tmp)
    for length in range(1,11):
        for phone_number in number_list[length]:
            for i in range(length):
                if phone_number[:i+1] in check_number[i+1]:
                    return "NO"
            check_number[length][phone_number] = True
    return "YES"

if __name__ == "__main__":
    main()