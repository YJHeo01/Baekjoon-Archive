#https://github.com/YJHeo01

n = int(input())

def check_palindrome(s):
    ret_value = 0
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if ret_value == 1:
                return 2
            ret_value = 1
            if s[left+1] == s[right]:
                left += 1
            elif s[left] == s[right-1]:
                right -= 1
            else:
                return 2
    return ret_value
        
for _ in range(n):
    sentence = list(input())
    print(check_palindrome(sentence))