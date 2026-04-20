#include <stdio.h>
#include <stdlib.h>
int main() {
	int n,tmp,x;
	int idx = -1;
	scanf("%d", &n);
	int* stack = (int*)malloc(sizeof(int) * n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &tmp);
		switch (tmp)
		{
		case 1:
			idx++;
			scanf("%d", &x);
			*(stack + 4 * idx) = x;
			break;
		case 2:
			if (idx == -1) {
				printf("-1\n");
			}
			else {
				printf("%d\n", *(stack + 4 * idx));
				idx--;
			}
			break;
		case 3:
			printf("%d\n", idx + 1);
			break;
		case 4:
			if (idx == -1) {
				printf("1\n");
			}
			else {
				printf("0\n");
			}
			break;
		case 5:
			if (idx != -1) {
				printf("%d\n", *(stack + 4 * idx));
			}
			else {
				printf("-1\n");
			}
		default:
			break;
		}
	}

}