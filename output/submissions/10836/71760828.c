#define MAX(a,b) a > b ? a : b
#include <stdio.h>

int answer[700][700] = { 0, };

int main() {
	int m, n;
	scanf("%d %d", &m, &n);
	for (int i = 0; i < n; i++) {
		int idx, one, two;
		scanf("%d %d %d", &idx, &one, &two);
		for (int j = 0; j < one; j++) {
			if (idx < m) {
				answer[m - 1 - idx][0]++;
			}
			else {
				answer[0][idx - m + 1]++;
			}
			idx++;
		}
		for (int j = 0; j < two; j++) {
			if (idx < m) {
				answer[m - 1 - idx][0] += 2;
			}
			else {
				answer[0][idx - m + 1] += 2;
			}
			idx++;
		}
	}
	for (int i = 1; i < m; i++) {
		for (int j = 1; j < m; j++) {
			answer[i][j] = MAX(answer[i - 1][j], answer[i][j - 1]);
		}
	}
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < m; j++) {
			printf("%d ", answer[i][j] + 1);
		}
		printf("\n");
	}
}