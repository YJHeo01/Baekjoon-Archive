#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);
	int answer = 665;
	while (n > 0) {
		answer++;
		int tmp = answer;
		int six_cnt = 0;
		while (tmp > 0) {
			if (tmp % 10 == 6) {
				six_cnt++;
				if (six_cnt >= 3) {
					n--;
					break;
				}
			}
			else {
				six_cnt = 0;
			}
			tmp /= 10;
		}
	}
	printf("%d", answer);
}