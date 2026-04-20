//https://github.com/YJHeo01
#include <stdio.h>

int main() {
	int t;
	scanf("%d", &t);
	while (t--) {
		int n;
		scanf("%d", &n);
		int coin_array[20] = { 0, };
		for (int i = 0; i < n; i++) {
			scanf("%d ", &coin_array[i]);
		}
		int m;
		scanf("%d", &m);
		int dp[10001] = { 0, };
		dp[0] = 1;
		for (int i = 0; i < n; i++) {
			for (int j = coin_array[i]; j <= m; j++) {
				if (dp[j - coin_array[i]] != 0) {
					dp[j] += dp[j - coin_array[i]];
				}
			}
		}
		printf("%d\n", dp[m]);
	}
}