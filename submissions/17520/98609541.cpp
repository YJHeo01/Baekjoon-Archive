#define INF 16769023

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int dp[100001][3] = { 0, };

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;

    cin >> n;

    dp[1][1] = 1;
    dp[1][0] = 1;
    for (int i = 1;i < 100000;i++) {
        dp[i + 1][2] = dp[i][1] + dp[i][0];
        dp[i + 1][1] = dp[i][2];
        dp[i + 1][0] = dp[i][2];
        dp[i + 1][2] %= INF;
    }

    int answer = dp[n][0] + dp[n][1] + dp[n][2];
    answer %= INF;

    cout << answer;

    return 0;
}