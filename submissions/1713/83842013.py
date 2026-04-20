def main():
    n = int(input())
    length = int(input())
    first_recommend_time = [length] * 101
    picture_box = [0] * 101
    picture_box[0] = 987654321
    box_size = 0
    array = list(map(int,input().split()))
    
    for time in range(length):
        idx = array[time]
        if first_recommend_time[idx] == length: box_size += 1
        if picture_box[idx] == 0 and box_size > n:
            remove_idx = 0
            for i in range(101):
                if picture_box[i] == 0: continue
                if picture_box[remove_idx] == picture_box[i] and first_recommend_time[remove_idx] > first_recommend_time[i]:
                    remove_idx = i
                    continue
                if picture_box[remove_idx] > picture_box[i]:
                    remove_idx = i
            first_recommend_time[remove_idx] = length
            picture_box[remove_idx] = 0
        picture_box[idx] += 1
        first_recommend_time[idx] = min(first_recommend_time[idx],time)
    
    for i in range(1,101):
        if picture_box[i] != 0:
            print(i,end=" ")

if __name__ == "__main__":
    main()