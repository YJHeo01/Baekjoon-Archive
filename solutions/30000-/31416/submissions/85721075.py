import sys

input = sys.stdin.readline

def main():
    q = int(input())
    for _ in range(q):
        ta,tb,va,vb = map(int,input().split())
        time_a, time_b = ta * va, tb * vb
        if time_b >= time_a:
            print(time_b)
            continue
        a_cnt, b_cnt = 0,0
        for i in range(1,20001):
            if i % ta == 0: a_cnt += 1
            if i % tb == 0: b_cnt += 1
            #if a_cnt > va and (i - time_a) % tb == 0: b_cnt += 1
            if b_cnt > vb and (i - time_b) % ta == 0: a_cnt += 1
            if a_cnt >= va and b_cnt >= vb:
                print(i)
                break

if __name__ == "__main__":
    main()