def main(): 
    information = get_information()
    answer = solution(information)
    print(answer)

def get_information():
    ret_value = []
    for _ in range(n):
        a,b = map(int,input().split())
        if a > b: a,b = b,a
        ret_value.append((a,b))
    ret_value = sorted(ret_value, key = lambda x : x[1])
    return ret_value

def solution(information):
    d = int(input())
    ret_value = binary_search(information,0,d)
    for i in range(1,n):
        if information[i][0] == information[i-1][0]: continue
        ret_value = max(ret_value,binary_search(information,i,d))
    return ret_value

def binary_search(information,idx,d):
    home = information[idx][0]
    left, right = idx, n - 1
    ret_value = idx
    while left <= right:
        mid = (left+right) // 2
        if home + d >= information[mid][1]:
            ret_value = mid
            left = mid + 1
        else:
            right = mid - 1
    ret_value += 1
    array = information[idx:ret_value]
    array.sort()
    left, right = 0, ret_value - idx
    target = -1
    while left <= right:
        mid = (left+right) // 2
        if array[mid][0] < home:
            target = mid
            left = mid + 1
        else:
            right = mid - 1
    ret_value -= (target + 1 + idx)
    return ret_value

if __name__ == "__main__":
    n = int(input())
    main()