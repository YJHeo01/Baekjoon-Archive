#include <stdio.h>

int _array[10000] = { 0, };
int prefix_sum[10001] = { 0, };

int find_left_idx(int right_idx, int target_value) {
	int left = 0;
	int right = right_idx;
	int ret_value = right_idx;
	while (left <= right) {
		int left_idx = (left+right)/2;
		int value = prefix_sum[right_idx] - prefix_sum[left_idx];
		if (value > target_value) {
			left = left_idx + 1;			
		}
		else if(value < target_value) {
			right = left_idx - 1;
		}
		else {
			ret_value = left_idx;
			break;
		}
	}
	return ret_value;
}
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
		int left = find_left_idx(right, m);
		if (prefix_sum[right] - prefix_sum[left] == m) {
			answer++;
		}
	}
	printf("%d", answer);
}