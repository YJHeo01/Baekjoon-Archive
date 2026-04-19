#include <stdio.h>

int dp[100001][2] = { 0, };

int main() {
	dp[1][1] = 1; dp[2][1] = 1; dp[2][0] = 1;
	dp[3][1] = 2; dp[3][0] = 2;
	for (int i = 4; i <= 100000; i++) {
		for (int plus = 1; plus <= 3; plus++) {
			dp[i][0] += dp[i - plus][1];
			dp[i][1] += dp[i - plus][0];
			dp[i][0] %= 1000000009;
			dp[i][1] %= 1000000009;
		}
	}
	int t = 0;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		int n;
		scanf("%d", &n);
		printf("%d %d\n", dp[n][1], dp[n][0]);
	}
}