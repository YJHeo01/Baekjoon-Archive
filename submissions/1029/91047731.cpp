#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

#define INF 100000000

int dp[1 << 16][16] = { INF, };

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    char adj_matrix[16][16] = { 0, };

    for (int i = 0;i < n;i++) {
        cin >> adj_matrix[i];
    }

    for (int i = 0;i < (1 << n);i++) fill(dp[i], dp[i] + n, INF);

    dp[1][0] = 0;

    int answer = 1;

    for (int bit_mask = 1;bit_mask < (1 << n);bit_mask++) {
        for (int i = 0;i < n;i++) {
            if (dp[bit_mask][i] == INF) continue;
            int tmp = 0;
            for (int j = 0;j < n;j++) {
                if (bit_mask & (1 << j)) { tmp++; continue; }
                if (adj_matrix[i][j] - '0' < dp[bit_mask][i]) continue;
                int next_bit_mask = bit_mask | (1 << j);
                dp[next_bit_mask][j] = min(dp[next_bit_mask][j], adj_matrix[i][j] - '0');
            }
            answer = max(answer, tmp);
        }
    }
    cout << answer;
}