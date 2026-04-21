#include <stdio.h>

int arr[500000] = { 0, };

int main() {
	int n, m;
	scanf("%d %d", &n, &m);
	for (int i = 0;i < n;i++) {
		scanf("%d", &arr[i]);
	}

	int left = 0, right = 0;
	int tmp = arr[0];
	int answer = 0;
	if (tmp < m) answer = tmp;
	while (1) {
		if (right >= n) break;
		if (tmp > m) {
			tmp -= arr[left];
			left++;
		}
		else {
			if (tmp > answer) answer = tmp;
			tmp += arr[++right];
		}
	}

	printf("%d", answer);
}
