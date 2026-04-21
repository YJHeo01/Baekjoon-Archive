#include <stdio.h>

int main() {
	while (1) {
		int flag[11] = { 0, };
		int answer = 1;
		while (1) {
			int n;
			scanf("%d", &n);
			if (n == 0) return 0;
			char a[10] = { 0, };
			char b[10] = { 0, };
			scanf("%s %s", a, b);
			if (a[0] == 'r') {
				if (flag[n] == -1) {
					answer = 0;
				}
				break;
			}
			else if (b[0] == 'h') {
				for (int i = n;i <= 10;i++) flag[i] = -1;
			}
			else {
				for (int i = 1;i <= n;i++) flag[i] = -1;
			}

		}
		if (answer == 1) printf("Stan may be honest\n");
		else printf("Stan is dishonest\n");
	}
	return 0;
}