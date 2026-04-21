#include <iostream>
#include <algorithm>
#define INF (~0U>>2)
using namespace std;
int N, K, arr[101], dp[101][10001];
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> K;

    for (int i = 0; i <= N; i++) {
        for (int j = 0; j <= K; j++) {
            if (j == 0) dp[i][j] = 0;
            else dp[i][j] = INF;
        }
    }

    for (int i = 1; i <= N; i++) {
        cin >> arr[i];
    }

    sort(arr + 1, arr + N + 1);

    for (int i = 1; i <= N; i++) {
        if (arr[i] > K) continue;
        for (int j = 1; j <= K; j++) {
            if (j < arr[i]) dp[i][j] = dp[i - 1][j];
            else if (j == arr[i]) dp[i][j] = 1;
            else {
                dp[i][j] = min({ dp[i][j], dp[i - 1][j], dp[i][j - arr[i]] + 1, dp[i - 1][j - arr[i]] + 1 });
            }
        }
    }
    int ans = INF;
    for (int i = 1; i <= N; i++) {
        if (dp[i][K] == 0) continue;
        ans = min(ans, dp[i][K]);
    }
    cout << (ans == INF ? -1 : ans);
}