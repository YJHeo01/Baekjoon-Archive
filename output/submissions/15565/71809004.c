#define MIN(a,b) a > b ? b : a
#define INF 1000009
#include <stdio.h>

char information[1000000] = { 0, };

int main() {
	int n, k;
	scanf("%d %d", &n, &k);
	for (int i = 0; i < n; i++) {
		scanf(" %c", &information[i]);
	}
	int answer = INF;
	int left = 0;
	int right = 1;
	int cnt = 0;
	if (information[0] == '1') {
		cnt = 1;
	}
	while (right <= n) {
		if (cnt < k) {
			if (information[right++] == '1') {
				cnt++;
			}
		}
		else {
			answer = MIN(answer, right - left);
			if (information[left++] == '1') {
				cnt--;
			}
		}
	}
	if (answer == INF) {
		answer = -1;
	}
	printf("%d", answer);
}