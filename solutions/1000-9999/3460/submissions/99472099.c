#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 0;i < t;i++) {
		int n;
		scanf("%d", &n);
		for (int j = 0;j < 30;j++) {
			if (n & (1 << j)) printf("%d ", j);
		}
		printf("\n");
	}
}
