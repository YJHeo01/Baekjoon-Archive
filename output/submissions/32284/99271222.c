#include <stdio.h>

int main() {
	int n, m;
	scanf("%d %d", &n, &m);
	int a, b;
	scanf("%d %d", &a, &b);
	for (int i = 0;i < n;i++) {
		for (int j = 0;j < m;j++) {
			if (a > i) {
				printf("S");
			}
			else if (a < i) {
				printf("N");
			}
			else if (b < j) {
				printf("W");
			}
			else {
				printf("E");
			}
		}
		printf("\n");
	}
}