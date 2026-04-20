#include <string.h>
#include <stdio.h>

int main() {
	char s[100] = { 0, };
	scanf("%s", &s);
	int length = strlen(s);
	int mid = length / 2;
	for (int i = 0; i < mid; i++) {
		if (s[i] != s[length - i - 1]) {
			printf("0");
			return 0;
		}
	}
	printf("1");
}