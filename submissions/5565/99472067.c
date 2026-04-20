#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int a;
	scanf("%d", &a);
	for (int i = 0;i < 9;i++) {
		int tmp;
		scanf("%d", &tmp);
		a -= tmp;
	}
	printf("%d", a);
	
}
