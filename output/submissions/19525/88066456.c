#include <stdio.h>

int main() {
	char array[150][150];
	for (int i = 0;i < 150;i++) {
		for (int j = 0;j < 150;j++) {
			array[i][j] = 'o';
		}
	}
	for (int i = 0;i < 150;i++) {
		for (int j = i + 1;j < 150;j++) {
			for (int k = 0;k < 150;k++) {
				for (int l = k + 1;l < 150;l++) {
					array[i][j] = '.';
				}
			}
		}
	}
	int cnt = 0;
	printf("150\n");
	for (int i = 0;i < 150;i++) {
		for (int j = 0;j < 150;j++) {
			printf("%c", array[i][j]);
		}
		printf("\n");
	}
}