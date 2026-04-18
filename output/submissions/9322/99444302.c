#include <stdio.h>

int main() {

	int t;
	scanf("%d", &t);

	for (int i = 0;i < t;i++) {
		int n;
		scanf("%d", &n);
		char one[1000][11] = { 0, };
		char two[1000][11] = { 0, };
		char rule[1000] = { 0, };
		for (int j = 0;j < n;j++) scanf("%s", one[j]);
		for (int j = 0;j < n;j++) scanf("%s", two[j]);
		for (int j = 0;j < n;j++) {
			for (int k = 0;k < n;k++) {
				int tmp = 1;
				for (int l = 0;l < 11;l++) {
					if (one[j][l] != two[k][l]) tmp = 0;
				}
				if (tmp == 1) {
					rule[j] = k;
					break;
				}
			}
		}
		char s[1000][11] = { 0, };
		for (int j = 0;j < n;j++) scanf("%s", s[j]);
		for (int j = 0;j < n;j++) printf("%s ", s[rule[j]]);
		printf("\n");
	}
}
