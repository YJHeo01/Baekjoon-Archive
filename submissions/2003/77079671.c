#include <stdio.h>

int _array[10000] = { 0, };
int prefix_sum[10001] = { 0, };

int main() {
	int n, m;
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++) {
		scanf("%d", &_array[i]);
		prefix_sum[n] += _array[i];
	}
	for (int i = n - 1; i >= 0; i--) {
		prefix_sum[i] = prefix_sum[i + 1] - _array[i];
	}
	int answer = 0;
	for (int right = 1; right <= n; right++) {
		for (int left = 0; left < right; left++) {
			int value = prefix_sum[right] - prefix_sum[left];
			if (value > m) {
				continue;
			}
			else if (value < m) {
				break;
			}
			else {
				answer++;
			}
		}
	}
	printf("%d", answer);
}