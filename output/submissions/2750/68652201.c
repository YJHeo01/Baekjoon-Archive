#include <stdio.h>

int main() {
	int num[1001] = { 0 };
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &num[i]);
	}
	int tmp = 0;
	for (int i = n - 1; i > 0; i--) {
		for (int j = 0; j < i; j++) {
			if (num[j] > num[j + 1]) {
				tmp = num[j];
				num[j] = num[j + 1];
				num[j + 1] = tmp;
			}
		}
	}
	for (int i = 0; i < n; i++) {
		printf("%d\n", num[i]);
	}
}