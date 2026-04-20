#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int dp[12] = { 0, };
    dp[0] = 1;

    for (int i = 1;i <= 11;i++) {
        for (int j = 1;j <= 3;j++) {
            if (i - j < 0) continue;
            dp[i] += dp[i - j];
        }
    }

    int T;

    cin >> T;

    for (int i = 0;i < T;i++) {
        int n;
        cin >> n;
        cout << dp[n] << "\n";
    }

}