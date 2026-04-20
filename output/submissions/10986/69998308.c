#include <stdio.h>

int num[100000] = { 0, };
int prefix_sum[100001] = { 0, };

void main(void) {

	int n, m;
	scanf("%d %d", &n, &m);
	int sum = 0;
	for (int i = 0; i < n; i++) {
		scanf("%d", &num[i]);
		sum += num[i];
	}
	for (int i = n; i > 0; i--) {
		prefix_sum[i] = sum;
		sum -= num[i - 1];
	}
	int answer = 0;
	for (int i = 1; i <= n; i++) {
		for (int j = 0; j < i; j++) {
			if ((prefix_sum[i] - prefix_sum[j]) % m == 0) {
				answer += 1;
			}
		}
	}
	printf("%d", answer);
}