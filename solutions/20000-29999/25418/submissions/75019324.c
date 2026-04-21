#define MIN(a,b) a > b ? b : a
#define MAX(a,b) a > b ? a : b
#include <stdio.h>
#include <stdlib.h>

int dp[1000001] = { 0, };

int main() {
	int a, k;
	scanf("%d %d", &a, &k);
	for (int i = a+1; i <= 2 * a; i++) {
		dp[i] = dp[i - 1] + 1;
	}
	for (int i = 2 * a; i <= k; i++) {
		if (i % 2 == 0) {
			dp[i] = MIN(dp[i / 2], dp[i - 1]) + 1;
		}
		else {
			dp[i] = dp[i - 1] + 1;
		}
	}
	printf("%d", dp[k]);
}