#include <iostream>
#include <algorithm>
#include <vector>
#define INF 100000000

using namespace std;
int dp[1 << 16][16] = { INF, };

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int adj_matrix[16][16] = { 0, };

    for (int i = 0;i < n;i++) {
        for (int j = 0;j < n;j++) {
            cin >> adj_matrix[i][j];
        }
    }

    for (int i = 0;i < (1 << n);i++) {
        fill(dp[i], dp[i] + 16, INF);
    }

    dp[1][0] = 0;

    for (int bit_mask = 0;bit_mask < (1 << n);bit_mask++) {
        for (int i = 0;i < n;i++) {
            if (dp[bit_mask][i] == INF) continue;
            for (int j = 0;j < n;j++) {
                if (bit_mask & (1 << j) or adj_matrix[i][j] == 0) continue;
                int next_bit_mask = bit_mask | (1 << j);
                dp[next_bit_mask][j] = min(dp[next_bit_mask][j], dp[bit_mask][i] + adj_matrix[i][j]);
            }
        }
    }

    int answer = INF;

    for (int i = 1;i < n;i++) {
        if (adj_matrix[i][0] == 0) continue;
        answer = min(answer, dp[(1 << n) - 1][i] + adj_matrix[i][0]);
    }

    cout << answer;
}