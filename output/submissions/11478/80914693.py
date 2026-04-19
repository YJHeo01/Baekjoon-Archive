def main():
    print(solution(input()))

def solution(s):
    array = {}
    length = len(s)
    for right in range(length+1):
        for left in range(right):
            if s[left:right] not in array:
                array[s[left:right]] = 1
    return len(array)

if __name__ == "__main__":
    main()