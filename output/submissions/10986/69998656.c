#include <stdio.h>

int prefix_sum[100001] = { 0, };

void main(void) {
	int answer = 0;
	int n, m;
	scanf("%d %d", &n, &m);
	int sum = 0;
	for (int i = 1; i <= n; i++) {
		scanf("%d", &prefix_sum[i]);
		prefix_sum[i] += prefix_sum[i - 1];
		prefix_sum[i] = prefix_sum[i] % m;
	}
	for (int i = 1; i <= n; i++) {
		for (int j = 0; j < i; j++) {
			if ((prefix_sum[i] - prefix_sum[j]) % m == 0) {
				answer += 1;
			}
		}
	}
	printf("%d", answer);
}