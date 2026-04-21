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
	for (int i = 0; i <= n-2; i++) {
		for(int j = n-2;j>=i;j--)
		{
			if (a[j] > a[j + 1]) {
				str_change(b[j], b[j + 1]);
				tmp = a[j];
				a[j] = a[j + 1];
				a[j + 1] = tmp;
			}
		}
	}
	for (int i = 0; i < n; i++) {
		printf("%d %s\n", a[i],b[i]);
	}
}