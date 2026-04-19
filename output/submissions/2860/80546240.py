def main():
    target = float(input())
    answer = init_answer(target)
    sum_value = init_sum_value(answer)
    cnt = 1
    while True:
        if sum_value / cnt == target:
            break
        tmp = 6
        next_idx = 0
        for i in range(1,6):
            next_avg = (sum_value+i) / (cnt+1)
            if tmp > abs(target-next_avg):
                tmp = abs(target-next_avg)
                next_idx = i
        answer[next_idx] += 1
        sum_value += next_idx
        cnt += 1
    print(*answer[1:])
    
def init_answer(target):
    idx = 0
    for i in range(1,6):
        if target - idx > target - i:
            idx = i
    answer = [0] * 6
    answer[idx] = 1
    return answer

def init_sum_value(answer):
    for i in range(1,6):
        if answer[i] == 1:
            return i
if __name__ == "__main__":
    main()