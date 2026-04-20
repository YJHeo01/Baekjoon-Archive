#define MAX(a,b) a > b ? a : b
#include <stdio.h>

int answer[701][701] = { 0, };

int main() {
	int m, n;
	scanf("%d %d", &m, &n);
	for (int i = 0; i < n; i++) {
		int idx, one, two;
		scanf("%d %d %d", &idx, &one, &two);
		for (int j = 0; j < one; j++) {
			if (idx < m) {
				answer[m - idx][1]++;
			}
			else {
				answer[1][idx - m + 2]++;
			}
			idx++;
		}
		for (int j = 0; j < two; j++) {
			if (idx < m) {
				answer[m - idx][1] += 2;
			}
			else {
				answer[1][idx - m + 2] += 2;
			}
			idx++;
		}
	}
	for (int i = 1; i <= m; i++) {
		printf("%d ", answer[1][i]+1);
	}
	printf("\n");
	for (int i = 2; i <= m; i++) {
		printf("%d ", answer[i][1]+1);
		for (int j = 2; j <= m; j++) {
			answer[i][j] = MAX(answer[i - 1][j], answer[i][j - 1]);
			printf("%d ", answer[i][j]+1);
		}
		printf("\n");
	}

}