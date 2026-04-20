#include <stdio.h>
#include <math.h>

int main() {
	int t, n;
	scanf("%d %d", &t, &n);
	int restrain[52] = { 0, };
	for (int i = 0; i < n; i++) {
		int value = 0;
		int cnt;
		scanf("%d", &cnt);
		for (int j = 0; j < cnt; j++) {
			int tmp;
			scanf("%d", &tmp);
			value += (int)pow(2,--tmp);
		}
		restrain[i] = value;
	}
	int answer = 0;
	for (int i = 0; i < (int)pow(2, t); i++) {
		answer += 1;
		for (int j = 0; j < n; j++) {
			if ((i & restrain[j]) == restrain[j]) {
				answer -= 1;
				break;
			}
		}
	}
	printf("%d", answer);
}