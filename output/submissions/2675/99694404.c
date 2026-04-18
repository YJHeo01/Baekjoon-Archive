#include <stdio.h>

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 0;i < t;i++) {
		int cnt;
		char s[30] = { 0, };
		scanf("%d %s", &cnt, s);
		for (int j = 0;j < 30;j++) {
			if (s[j] == 0) break;
			for (int k = 0;k < cnt;k++) {
				printf("%c", s[j]);
			}
		}
		printf("\n");
	}
	return 0;
}