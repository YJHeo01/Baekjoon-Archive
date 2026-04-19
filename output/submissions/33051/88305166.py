import sys

input = sys.stdin.readline

def main():
    n,k,m = map(int,input().split())
    base_score = [0] * 5
    rank_cnt = [[0]*5 for _ in range(5)]
    for _ in range(n):
        tmp = list(map(int,input().split()))
        for i in range(4):
            base_score[i] += tmp[i+4]
            rank_cnt[i+1][tmp[i]] += 1
    for d4 in range(-100,101):
        for d3 in range(d4,101):
            for d2 in range(d3,101):
                d1 = -d2-d3-d4
                if d1 + d2 + d3 + d4 != 0 or d1 < d2: continue
                score_list = []
                for i in range(1,5):
                    tmp = base_score[i]
                    tmp += rank_cnt[i][1] * d1
                    tmp += rank_cnt[i][2] * d2
                    tmp += rank_cnt[i][3] * d3
                    tmp += rank_cnt[i][4] * d4
                    score_list.append(tmp)
                sorted_score_list = sorted(score_list,reverse=True)
                target_rank = 0
                for i in range(4):
                    if sorted_score_list[i] == score_list[k]:
                        target_rank = i + 1
                        break
                if target_rank == m:
                    print(d1,d2,d3,d4)
                    return
    print(-1)
                
if __name__ == "__main__":
    main()