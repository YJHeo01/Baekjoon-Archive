#include <stdio.h>

int main() {
	unsigned int s;
	scanf("%d", &s);
	unsigned int n = 0;
	while (1) {
		if (s < n) {
			n--;
			break;
		}
		s -= n++;
	}
	printf("%d", n);
}