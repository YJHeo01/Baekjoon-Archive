#include <stdio.h>


int main()
{
	int h, m;
	scanf("%d %d", &h, &m);
	if (m >= 45) {
		m = m - 45;
	}
	else if (h > 0) {
		m = m + 15;
		h--;
	}
	else {
		h = 23;
		m = m + 15;
	}
	printf("%d %d", h, m);
}