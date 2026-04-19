import sys

input = sys.stdin.readline

def main():
    n = int(input())
    yes_jam_book, no_jam_book = [], []
    cur_happy = 0
    for _ in range(n):
        a,b = map(int,input().split())
        if a <= b:
            yes_jam_book.append((a,-b))
        else:
            no_jam_book.append((-a,-b))
    yes_jam_book.sort(); no_jam_book.sort()
    answer = 1
    for a,b in yes_jam_book:
        cur_happy -= a
        if cur_happy < 0: answer = 0
        cur_happy -= b
    for a,b in no_jam_book:
        cur_happy += a
        cur_happy -= b
    if cur_happy < 0: answer = 0
    print(answer)

if __name__ == "__main__":
    main()