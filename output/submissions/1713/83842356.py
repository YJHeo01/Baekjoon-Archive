def main():
    n = int(input())
    max_time = int(input())
    recommend_time = [max_time] * 101
    recommend_cnt = [0] * 101 #과정 1 : 모든 사진틀이 비어있음
    recommend_cnt[0] = 987654321
    box_size = 0
    array = list(map(int,input().split()))
    
    for time in range(max_time):
        idx = array[time]
        if recommend_time[idx] == max_time: box_size += 1
        if recommend_cnt[idx] == 0 and box_size > n: # 과정 3 : 비어있는 사진틀이 없는 경우
            del_idx = 0
            for i in range(101):
                if recommend_cnt[i] == 0: continue
                if (recommend_cnt[del_idx] == recommend_cnt[i] and recommend_time[del_idx] > recommend_time[i]) or recommend_cnt[del_idx] > recommend_cnt[i]:
                    del_idx = i
            recommend_time[del_idx] = max_time
            recommend_cnt[del_idx] = 0 # 과정 5 : 사진 삭제 후 추천횟수 0
        recommend_cnt[idx] += 1 # 과정 2, 4 : 추천받은 사진이 사진틀에 게시되고, 이미 있는 경우 추천횟수 증가
        recommend_time[idx] = min(recommend_time[idx],time)
    
    for i in range(1,101):
        if recommend_cnt[i] != 0:
            print(i,end=" ")

if __name__ == "__main__":
    main()