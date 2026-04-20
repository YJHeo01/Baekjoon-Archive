t = int(input())
for _ in range(t):
    string = list(input())
    l = len(string)
    answer = 0
    left, right = 0,l-1
    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        elif string[left] == string[right-1]:
            right -= 1
            answer += 1
        elif string[left+1] == string[right]:
            left += 1
            answer += 1
        else:
            answer = 2
            break
        if answer == 2:
            break
    print(answer)