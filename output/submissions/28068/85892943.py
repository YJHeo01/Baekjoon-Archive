import sys

input = sys.stdin.readline

def main():
    n = int(input())
    yes_jam_book, no_jam_book = [], []
    cur_happy, need_max_happy = 0, 0
    for _ in range(n):
        a,b = map(int,input().split())
        if a < b:
            yes_jam_book.append((a,b))
        elif a > b:
            no_jam_book.append((-a,-b))
        else:
            need_max_happy = max(need_max_happy,a)
    yes_jam_book.sort(); no_jam_book.sort()
    answer = 1
    for a,b in yes_jam_book:
        if a > cur_happy:
            answer = 0
            break
        cur_happy -= a
        cur_happy += b
    if cur_happy < need_max_happy:
        answer = 0
    for a,b in no_jam_book:
        cur_happy += a
        if cur_happy < 0:
            answer = 0
        cur_happy -= b
    print(answer)

if __name__ == "__main__":
    main()