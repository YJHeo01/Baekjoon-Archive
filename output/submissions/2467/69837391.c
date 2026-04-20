#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int ph[100000] = { 0, };

int main() {
	int n = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &ph[i]);
	}
	int answer1, answer2, tmp;
	int answer_val = 2000000001;
	int left = 0;
	int right = n - 1;
	while (left < right) {
		tmp = ph[right] + ph[left];
		if (abs(tmp) < answer_val) {
			answer1 = left;
			answer2 = right;
			answer_val = abs(tmp);
		}
		if (tmp < 0) {
			left++;
		}
		else if(tmp>0) {
			right--;
		}
		else {
			break;
		}
	}
	printf("%d %d", ph[answer1], ph[answer2]);
}