def main():
    s = list(input())
    answer = get_answer(s)
    print(answer)

def get_answer(s):
    if s[0] == '0': return 0
    length = len(s)
    if length == 1: return 1
    dp = [[0] * 2 for _ in range(length)]
    dp[0][0] = 1
    for i in range(1,length):
        if s[i-1] == '1' or (s[i-1]=='2' and int(s[i])<= 6):
            dp[i][1] += dp[i-1][0]; dp[i][1] %= 1000000
        if s[i] == '0':
            if s[i-1] == '0': return 0
            continue
        dp[i][0] += sum(dp[i-1]); dp[i][0] %= 1000000
    return sum(dp[length-1])

if __name__ == "__main__":
    main()