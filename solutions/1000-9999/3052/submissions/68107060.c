#include <stdio.h>


int main()
{
	int mod[42];
	int n;
	int i;
	for (i = 0; i <= 9; i++) {
		scanf("%d", &n);
		n = n % 42;
		mod[n] = 1;
	}
	n = 0;
	for (i = 0; i < 42; i++) {
		if (mod[i] == 1) {
			n++;
		}
	}
	printf("%d", n);
}