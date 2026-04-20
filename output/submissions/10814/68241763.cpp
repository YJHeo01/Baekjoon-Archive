#include <stdio.h>
#include <string.h>


int a[100000];
char b[100000][100];

int main()
{
	int n,tmp2 = 0;
	char tmp1 = 0;
	int s,z,l = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d %s", &a[i], b[i]);
	}
	for (int i = 0; i < n-2; i++) {
		for(int j = n-2;j>=i;j--)
		{
			if (a[j] > a[j + 1]) {
				s = strlen(b[j]);
				z = strlen(b[j + 1]);
				if (s < z) {
					l = z;
				}
				else {
					l = s;
				}
				for (int k = 0; k < l; k++) {
					tmp1 = b[j][k];
					b[j][k] = b[j+1][k];
					b[j+1][k] = tmp1;
				}
				tmp2 = a[j];
				a[j] = a[j + 1];
				a[j + 1] = tmp2;
			}
		}
	}
	for (int i = 0; i < n; i++) {
		printf("%d %s\n", a[i],b[i]);
	}
}