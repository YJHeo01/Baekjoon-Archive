import sys, heapq

input = sys.stdin.readline

def main():
    n = int(input())
    yes_jam_book, no_jam_book = [], []
    for _ in range(n):
        a,b = map(int,input().split())
        if a <= b:
            yes_jam_book.append((a,-b))
        else:
            no_jam_book.append((-a,-b))
    yes_jam_book.sort(); no_jam_book.sort()
    print(solution(yes_jam_book,no_jam_book))

def solution(yes_jam_book,no_jam_book):
    cur_happy = 0
    for a,b in yes_jam_book:
        cur_happy = change_happy(cur_happy,a,b)
        if cur_happy < 0: return 0
    
    no_jam_cnt = len(no_jam_book)
    no_jam_read = [False]  * no_jam_cnt
    q = []
    
    for i in range(no_jam_cnt):
        a,b = no_jam_book[i]
        heapq.heappush(q,(b-a,i))
    
    for i in range(no_jam_cnt):
        a,b = no_jam_book[i]
        if no_jam_read[i]: continue
        while q:
            minus, idx = heapq.heappop(q)
            if no_jam_read[idx]: continue
            if cur_happy + minus < a:
                heapq.heappush(q,(minus,idx))
                break
            cur_happy += minus
            no_jam_read[idx] = True
        cur_happy = change_happy(cur_happy,-a,b)
        if cur_happy < 0: return 0
        no_jam_read[i] = True
    return 1

def change_happy(cur_happy,a,b):
    cur_happy -= a
    if cur_happy < 0: return -1
    return cur_happy - b

if __name__ == "__main__":
    main()