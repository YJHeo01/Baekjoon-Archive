#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	char s[101] = { 0, };
	scanf("%s", &s);
	int idx = 0;
	for (int i = 0;i < 101;i++) {
		if (s[i] == 0) break;
		idx = i;
	}
	int answer[100] = { 0, };

	for (int i = 0;i < 100;i++) answer[i] = -1;
	int answer_i = 0;

	while (1) {
		if (idx < 0) break;
		int tmp = 0;
		for (int i = 0;i < 3;i++) {
			if (idx >= i && s[idx - i] == '1') {
				tmp += (1 << i);
			}
		}
		answer[answer_i++] = tmp;
		idx -= 3;
	}

	for (int i = 80;i >= 0;i--) {
		if (answer[i] == -1) continue;
		printf("%d", answer[i]);
	}

}
