#include <stdio.h>

char arr[333335] = { 0, };

int main() {
	scanf("%s", arr);
	int idx = 0;
	if (arr[0] < '4') {
		if (arr[0] == '1') {
			printf("1");
		}
		else if (arr[0] == '2') {
			printf("10");
		}
		else if (arr[0]=='3') {
			printf("11");
		}
		else {
			printf("0");
		}
		idx = 1;
	}
	while (1) {
		if (arr[idx] == 0) break;
		int tmp = arr[idx] - '0';
		for (int i = 2;i >= 0;i--) {
			if (tmp & (1 << i)) printf("1");
			else printf("0");
		}
		idx++;
	}
}