#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int cal(int a, int b, int c) {
	if (b == 1) {
		return a;
	}
	if (b % 2 == 1) {
		return (a*cal(a, b/2, c) * cal(a, b/2, c)%c);
	}
	else {
		return cal(a, b / 2, c) * cal(a, b / 2, c) % c;
	}
}

int main() {
	int answer = 0;
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);
	answer = cal(a, b, c);
	printf("%d", answer);
}