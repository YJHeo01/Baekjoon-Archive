#include <stdio.h>

int dp[1001][1001] = { 0, };

int main() {
	dp[0][0] = 1; dp[1][1] = 1; dp[2][1] = 1; dp[2][2] = 1;
	dp[3][1] = 1; dp[3][2] = 2; dp[3][3] = 1;
	for (int i = 4; i <= 1000; i++) {
		for (int cnt = 1; cnt < 1000; cnt++) {
			for (int plus = 1; plus <= 3; plus++) {
				dp[i][cnt + 1] += dp[i - plus][cnt];
				dp[i][cnt + 1] %= 1000000009;
			}
		}
	}
	int t = 0;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		int n, m;
		scanf("%d %d", &n, &m);
		printf("%d\n", dp[n][m]);
	}
}