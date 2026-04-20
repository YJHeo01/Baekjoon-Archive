#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main() {
	int swit[101];
	int left,right;
	int n;
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
			for (int j = switch_val; j <= n; j = j + switch_val) {
				swit[j]++;
			}
			break;
		case 2:
			left = switch_val - 1;
			right = switch_val + 1;
			while (left > 0 && right <= n) {
				if (swit[left] != swit[right]) {
					break;
				}
				left--;
				right++;
			}
			for (int j = left + 1; j < right; j++) {
				swit[j]++;
			}
			break;
		default:
			break;
		}
	}
	for (int i = 1; i <= n; i++) {
		printf("%d ", (swit[i]) % 2);
	}
}