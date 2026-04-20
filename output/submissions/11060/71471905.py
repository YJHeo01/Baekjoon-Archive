#define MIN(a,b) a > b ? b : a;
#define MAX(a,b) a > b ? a : b;
#define INF 987654321
#include <stdio.h>
int maze[1001] = { 0, };
int dp[1001] = { 0, };
int main() {
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		scanf("%d", &maze[i]);
		dp[i] = INF;
	}
	dp[1] = 0;
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= maze[i]; j++) {
			if (j + i > n) {
				break;
			}
			dp[i+j] = MIN(dp[i] + 1, dp[i+j]);
		}
	}
	int answer = dp[n];
	if (answer >= INF) {
		answer = -1;
	}

	printf("%d", answer);
}