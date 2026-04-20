#define MAX(a,b) a > b ? a : b
#include <stdio.h>

int main() {
	int n;
	int soldiers[2000] = { 0, };
	int dp[2000] = { 0, };
	scanf("%d", &n);
	for(int i=0;i<n;i++){
		scanf("%d", &soldiers[i]);
	}
	int answer = 1;
	dp[0] = 1;
	for (int i = 1; i < n; i++) {
		dp[i] = 1;
		for (int j = 0; j < i; j++) {
			if (soldiers[i] < soldiers[j]) {
				dp[i] = MAX(dp[i], dp[j] + 1);
			}
		}
		answer = MAX(answer, dp[i]);
	}
	printf("%d", n - answer);
}