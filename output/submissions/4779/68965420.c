#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void cantor(int first, int last, char chr) {
	if (first + 1 == last) {
		printf("%c", chr);
		return;
	}
	cantor(first, first + (last - first) / 3, chr);
	cantor(first + (last - first) / 3, first + 2 * (last - first) / 3, ' ');
	cantor(first + 2 * (last - first) / 3, last, chr);
	return;
}
int main() {
	int n;
	while (scanf("%d", &n)!=EOF) {
		cantor(0, (int)pow(3, n), '-');
		printf("\n");
	}
}