import sys

input = sys.stdin.readline

def main():
    n = int(input())
    company = set([])
    for _ in range(n):
        name, command = input().split()
        if command == "enter":
            company.add(name)
        else:
            company.remove(name)
    company = list(company)
    company.sort(reverse=True)
    for name in company:
        print(name)

if __name__ == "__main__":
    main()