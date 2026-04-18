#include <stdio.h>

int main() {
	int n, k;
	scanf("%d %d", &n, &k);
	int arr[1001] = { 0, };
	for (int i = 0;i < n;i++) scanf("%d", &arr[i]);
	for (int i = n - 1;i >= 0;i--) {
		for (int j = 0;j < i;j++) {
			if (arr[j + 1] > arr[j]) {
				int tmp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = tmp;
			}
		}
	}
	k--;
	printf("%d", arr[k]);
}