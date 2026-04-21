#include <stdio.h>

int main() {
	for (int i = 2992;i <= 9999;i++) {
		int a = i;
		int b = i;
		int c = i;
		int sum_a = 0;
		int sum_b = 0;
		int sum_c = 0;
		while (1) {
			if (a == 0) break;
			sum_a += (a % 10);
			a /= 10;
		}
		while (1) {
			if (b == 0) break;
			sum_b += (b % 12);
			b /= 12;
		}
		while (1) {
			if (c == 0) break;
			sum_c += (c % 16);
			c /= 16;
		}
		if (sum_a == sum_b && sum_b == sum_c) printf("%d\n", i);
	}
}