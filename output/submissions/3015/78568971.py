import sys

input = sys.stdin.readline

def main():
    n = int(input())
    array = get_array(n)
    answer = get_answer(array,n)
    print(answer)

def get_array(n):
    ret_value = []
    for _ in range(n):
        ret_value.append(int(input()))
    return ret_value

def get_answer(array,n):
    right_see_cnt = [0] * n
    answer = 0
    stack = []
    for r_idx in range(n):
        right = array[r_idx]
        while True:
            if stack == []:break
            answer += 1
            l_idx = stack.pop()
            left = array[l_idx]
            if left >= right:
                stack.append(l_idx)
                right_see_cnt[r_idx] = right_see_cnt[l_idx] + 1
                answer += right_see_cnt[r_idx]
                answer -= 1
                break
        stack.append(r_idx)
    return answer

if __name__ == "__main__":
    main()