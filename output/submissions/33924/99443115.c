#include <stdio.h>

char command[3000] = { 0, };

int main() {
	int n, m;
	scanf("%d %d", &n, &m);
	n -= 1; m -= 1;
	int k;
	scanf("%d", &k);
	scanf("%s", command);
	for (int i = 0;i < k;i++) {
		char c = command[i] - 'A';
		switch (c)
		{
		case 0:
			if (n < 2) n += 2;
			else n -= 2;
			break;
		case 1:
			m ^= 1;
			if (n % 2 == 0) n += 1;
			else n -= 1;
			break;
		case 2:
			m ^= 1;
			n = 3 - n;
			break;
		default:
			if (n == 0 && m == 0) m++;
			else if (n == 3 && m == 1) m--;
			else if (m == 1)n++;
			else n--;
			break;
		}
	}
	n += 1;
	m += 1;

	printf("%d %d", n, m);
}