#include <stdio.h>

int main()
{
	int t, h, w, n;
	scanf("%d", &t);
	int xx;
	int yy;
	for (int i = 0; i < t; i++) {
		scanf("%d %d %d", &h, &w, &n);
		xx = ((n - 1) / h) + 1;
		yy = ((n - 1) % h) + 1;
		if (xx < 10) {
			printf("%d0%d\n", yy, xx);
		}
		else {
			printf("%d%d\n", yy, xx);
		}
	}	
}