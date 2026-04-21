#include <iostream>
#include <algorithm>

#define INF 987654321
using namespace std;

int dp[201][201][3] = {0,};
int room[200][2] = { 0, };

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	for (int i = 0;i <= 200;i++) {
		for (int j = 0;j <= 200;j++) fill(dp[i][j], dp[i][j] + 3, -INF);
	}

	dp[0][0][0] = 0;

	while (true) {
		int N, k;
		cin >> N >> k;
		if (N == 0) break;
		for (int i = 0;i < N;i++) {
			for (int j = 0;j < 2;j++) cin >> room[i][j];
		}

		for (int i = 0;i < N;i++) {
			dp[i + 1][0][0] = dp[i][0][0] + room[i][0] + room[i][1];
			for (int j = 1;j <= k;j++) {
				dp[i + 1][j][0] = *max_element(dp[i][j], dp[i][j] + 3) + room[i][0] + room[i][1];
				dp[i + 1][j][1] = max(dp[i][j - 1][0], dp[i][j - 1][1]) + room[i][0];
				dp[i + 1][j][2] = max(dp[i][j - 1][0], dp[i][j - 1][2]) + room[i][1];
			}
		}

		int answer = *max_element(dp[N][k], dp[N][k] + 3);
		cout << answer << '\n';
	}

}