#define MAX(A,B) A > B ? A : B 
#include <stdio.h>

int snack[1000000] = { 0, };


int main() {
	int m, n;
	scanf("%d %d", &m, &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &snack[i]);
	}
	if (n >= m) {
		printf("%d", snack[n - m]);
	}
	else {
		int answer = 0;
		int left = 1;
		int right = snack[0];
		while (left <= right) {
			int mid = (left + right) / 2;
			int snack_cnt = 0;
			for (int i = 0; i < n; i++) {
				snack_cnt += (snack[i] / mid);
			}
			if (snack_cnt >= m) {
				answer = MAX(answer, mid);
				left = mid + 1;
			}
			else {
				right = mid - 1;
			}
		}
		printf("%d", answer);
	}
}