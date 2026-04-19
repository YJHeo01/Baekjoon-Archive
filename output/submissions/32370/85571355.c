#include <stdio.h>

int main()
{
	int a, b, x, y;
	scanf("%d %d", &a, &b);
	scanf("%d %d", &x, &y);

	if (a == 0) {
		if (x == 0 && b > y)printf("3");
		else printf("1");
	}
	else if (b == 0) {
		if (y == 0 && a > x) printf("3");
		else printf("1");
	}
	else {
		printf("2");
	}
}