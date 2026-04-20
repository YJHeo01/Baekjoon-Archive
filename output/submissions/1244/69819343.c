#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int swit[101];
int n;

void print_switch() {
	for (int i = 1; i <= n; i++) {
		printf("%d ", (swit[i]) % 2);
		if (i % 20 == 0) {
			printf("\n");
		}
	}
}

void man(int value) {
	for (int j = value; j <= n; j = j + value) {
		swit[j]++;
	}
	return;
}

void woman(int value) {
	int left = value - 1;
	int right = value + 1;
	while (left > 0 && right <= n) {
		if ((swit[left])%2 != (swit[right])%2) {
			break;
		}
		left--;
		right++;
	}
	for (int j = left + 1; j < right; j++) {
		swit[j]++;
	}
	return;
}


int main() {

	int left,right;

	scanf("%d", &n);
	for(int i=1;i<=n;i++){
		scanf("%d", &swit[i]);
	}
	int student,command,switch_val;
	scanf("%d", &student);
	for (int i = 0; i < student; i++) {
		scanf("%d %d", &command, &switch_val);
		switch (command)
		{
		case 1:
			man(switch_val);
			break;
		case 2:
			woman(switch_val);
			break;
		default:
			break;
		}
	}
	print_switch();
}