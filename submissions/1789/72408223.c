#include <stdio.h>

int main() {
	unsigned int s;
	scanf("%d", &s);
	unsigned int n = 0;
	while (1) {
		s -= ++n;
		if (s <= 0) {
			n--;
			break;
		}
	}
	printf("%d", n);
}