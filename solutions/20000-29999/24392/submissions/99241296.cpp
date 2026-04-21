#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#define INF 1000000007
using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    
    cin >> n >> m;

    vector<vector<int>> arr(n, vector<int>(m, 0));

    for (int i = 0;i < n;i++) {
        for (int j = 0;j < m;j++) {
            cin >> arr[n-1-i][j];
        }
    }

    vector<vector<int>> dp(n, vector<int>(m, 0));

    for (int j = 0;j < m;j++) dp[0][j] = arr[0][j];
    
    for (int i = 0;i < n - 1;i++) {
        for (int j = 0;j < m;j++) {
            if (dp[i][j] == 0) continue;
            for (int k = -1;k <= 1;k++) {
                int x = j + k;
                if (x < 0 or x >= m or arr[i+1][x]==0) continue;
                dp[i + 1][x] += dp[i][j];
                dp[i + 1][x] %= INF;
            }
        }
    }

    int answer = 0;

    for (int j = 0;j < m;j++) {
        answer += dp[n - 1][j];
        answer %= INF;
    }
    
    cout << answer;
    return 0;
}
