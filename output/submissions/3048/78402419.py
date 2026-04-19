def main():
    n1_cnt, n2_cnt = map(int,input().split())
    ant_cnt = n1_cnt + n2_cnt
    n1 = list(input()); n1.reverse()
    n2 = list(input())
    ant_list = []
    for c in n1: ant_list.append([c,'R'])
    for c in n2: ant_list.append([c,'L'])
    t = int(input())
    for _ in range(t):
        left = 0
        while True:
            if left >= ant_cnt: break
            if ant_list[left][1] == 'L': left += 1; continue
            right = left + 1
            if right >= ant_cnt: break
            if ant_list[right][1] == 'L':
                ant_list[left], ant_list[right] = ant_list[right], ant_list[left]
                left += 1
            left += 1
    for c,d in ant_list:print(c,end="")

if __name__ == "__main__":
    main()