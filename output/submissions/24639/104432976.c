#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>

int main()
{
	int n, m, c;
	scanf("%d", &n);
	scanf("%d", &m);
	scanf("%d", &c);
	int M = 0;
	int C = 0;
	for (int i = 0;i <= (n / m + 1);i++) {
		int tmp = n - m * i;
		for (int j = tmp / c;j <= tmp / c + 1;j++) {
			if (abs(M * m + C * c - n) > abs(i * m + j * c - n)) {
				M = i;
				C = j;
			}
		}
	}
	printf("%d %d", M, C);
}