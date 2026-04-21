#include <iostream>
#include <algorithm>
#include <vector>

#define INF 1000000000

using namespace std;

int dp[3000][3000][2] = { 0, };
int arr[3000] = { 0, };

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, b;
    cin >> n >> b;

    for (int i = 0;i < n;i++) cin >> arr[i];

    for (int i = 0;i < n;i++) {
        dp[i][0][0] = 0;
        dp[i][0][1] = -INF;
        for (int j = 1;j <= min(i+1,b);j++) {
            dp[i + 1][j][1] = max(dp[i][j - 1][1] + arr[i], dp[i][j-1][0]);
            dp[i + 1][j][0] = max(dp[i][j][0], dp[i][j][1]);
        }
    }

    cout << max(dp[n][b][0], dp[n][b][1]);
}