#include <stdio.h>


int main() {
	int h, w;
	int block[500] = { 0, };
	scanf("%d %d", &h, &w);
	for (int i = 0; i < w; i++) {
		scanf("%d", &block[i]);
	}
	int answer = 0;
	int left_block = -1;
	for (int i = 0; i <h; i++) {
		left_block = -1;
		for (int j = 0; j < w; j++) {
			if (block[j] > i) {
				if (left_block == -1) {
					left_block = j;
				}
				else {
					answer += (j - left_block-1);
					left_block = j;
				}
			}
		}
	}


	printf("%d", answer);
}