import sys

input = sys.stdin.readline

def main():
    n = int(input())
    member_list = [[] for _ in range(201)]
    for _ in range(n):
        age, name = input().split()
        member_list[int(age)].append(name)
    for age in range(1,201):
        for name in member_list[age]:
            print(age,name)

if __name__ == "__main__":
    main()