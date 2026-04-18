#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	
	int num[1000] = { 0, };
	int idx = 0;
	
	for (int i = 1;i < 1000;i++) {
		for (int j = 0;j < i;j++) {
			if (idx == 1000) break;
			num[idx++] = i;
		}
	}

	int a, b;
	scanf("%d %d", &a, &b);
	a -= 1; b -= 1;
	int answer = 0;
	for (int i = a;i <= b;i++) {
		answer += num[i];
	}
	printf("%d", answer);
	
}
