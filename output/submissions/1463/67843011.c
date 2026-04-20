#include <stdio.h>
#include <math.h>
int main() {
	
	int X;
	int cnt = 0;
	scanf("%d", &X);
	while (1) {
		if (X == 1) {
			break;
		}
		if (X % 3 == 0) {
			X = X / 3;
		}
		else if ((X-1) % 3 == 0) {
			X--;
		}
		else {
			X = X % 2;
		}
		cnt++;
		
	}
	printf("%d", cnt);
}