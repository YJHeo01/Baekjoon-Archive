#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

#define INF 1000000

int dp[100001] = { 0, };

int main() {
	
	int n;
	scanf("%d", &n);
	
	for (int i = 1;i <= n;i++) dp[i] = INF;
	
	for (int i = 0;i <= n;i++) {
		if (i + 5 <= n && dp[i + 5] > dp[i] + 1) dp[i + 5] = dp[i] + 1;
		if (i + 2 <= n && dp[i + 2] > dp[i] + 1) dp[i + 2] = dp[i] + 1;
	}

	int answer = dp[n];

	if (answer == INF) answer = -1;

	printf("%d", answer);
}