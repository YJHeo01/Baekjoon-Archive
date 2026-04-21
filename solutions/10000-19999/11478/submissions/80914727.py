def main():
    print(solution(input()))

def solution(s):
    array = {}
    length = len(s)
    answer = 0
    for right in range(length+1):
        for left in range(right):
            if s[left:right] not in array:
                array[s[left:right]] = 1
                answer += 1
    return answer

if __name__ == "__main__":
    main()