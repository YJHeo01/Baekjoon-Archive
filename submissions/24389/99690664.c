#include <stdio.h>

int main() {
	unsigned int n;
	scanf("%u", &n);
	unsigned int target = ~n;
	target++;
	int answer = 0;
	for (int i = 0;i < 32;i++) {
		unsigned int a = n & (1 << i);
		unsigned int b = target & (1 << i);
		if (a != b) answer++;
	}
	printf("%d", answer);
	return 0;
}