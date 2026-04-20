#include <stdio.h>

int main()
{
	int a, b, c, d, e;
	scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);
	int sum = 0;
	sum = sum + a * a;
	sum = sum + b * b;
	sum = sum + c * c;
	sum = sum + d * d;
	sum = sum + e * e;
	sum = sum % 10;
	printf("%d", sum);
}