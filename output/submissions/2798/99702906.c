#include <stdio.h>

int main() {
	int arr[100] = { 0, };
	int n, m;
	scanf("%d %d", &n, &m);
	for (int i = 0;i < n;i++) scanf("%d", &arr[i]);
	int answer = 0;
	for (int i = 0;i < n;i++) {
		for (int j = 0;j < n;j++) {
			for (int k = 0;k < n;k++) {
				if (i == j || j == k || k == i) continue;
				if (arr[i] + arr[j] + arr[k] > m) continue;
				int tmp = arr[i] + arr[j] + arr[k];
				if (tmp > answer) answer = tmp;
			}
		}
	}
	printf("%d", answer);
}