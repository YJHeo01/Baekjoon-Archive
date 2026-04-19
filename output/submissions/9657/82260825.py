def main():
    n = int(input())
    dp = [0] * (n+1)
    dp[0] = 2
    for vx in range(n+1):
        for dx in [1,3,4]:
            nx = vx + dx
            if nx <= n and dp[nx] == 0:
                for ddx in [1,3,4]:
                    x = nx - ddx
                    if x >= 0 and new_value(dp[vx]) != dp[x]:
                        dp[nx] = new_value(dp[vx])
                        break
                if dp[nx] == 0:
                    dp[nx] = dp[vx]
    if dp[n] == 2:
        print("CY")
    else:
        print("SK")

def new_value(x):
    if x == 1:
        return 2
    return 1

if __name__ == "__main__":
    main()