#define max(a, b) (((a) > (b)) ? (a) : (b))

#include <stdio.h>

int dp[201] = { 0, };

int main(void)
{
	int n, m;
	scanf("%d %d", &n, &m);
	while (m--) {
		int day, page;
		scanf("%d %d", &day, &page);
		for (int j = n;j >= 0;j--) {
			if (day > j)break;
			dp[j] = max(dp[j], dp[j - day] + page);
		}
	}
	int answer = 0;
	for (int i = 0;i <= n;i++) {
		answer = max(answer, dp[i]);
	}

	printf("%d", answer);
}