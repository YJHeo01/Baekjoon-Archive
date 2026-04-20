#include <stdio.h>

int str_change(char c[], char d[]) {
	char tmp;
	for (int i = 0; i <= 99; i++) {
		tmp = c[i];
		c[i] = d[i];
		d[i] = tmp;
	}
	return 0;
}

int a[100000];
char b[100000][100];

int main()
{
	int n,tmp = 0;

	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d %s", &a[i], b[i]);
	}
	for (int i = n-2; i >= 0; i--) {
		if (a[i] > a[i + 1]) {
			str_change(b[i], b[i + 1]);
			tmp = a[i];
			a[i] = a[i + 1];
			a[i + 1] = tmp;
		}
	}
	for (int i = 0; i < n; i++) {
		printf("%d %s\n", a[i],b[i]);
	}
}