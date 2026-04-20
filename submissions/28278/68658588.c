#include <stdio.h>
#include <stdlib.h>

int stack[1000000];
int main() {
	int n,tmp,x;
	int idx = -1;
	scanf("%d", &n);


	for (int i = 0; i < n; i++) {
		scanf("%d", &tmp);
		switch (tmp)
		{
		case 1:
			scanf("%d", &x);
			stack[++idx] = x;
			break;
		case 2:
			if (idx == -1) {
				printf("-1\n");
			}
			else {
				printf("%d\n", stack[idx--]);
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
				printf("%d\n", stack[idx]);
			}
			else {
				printf("-1\n");
			}
		default:
			break;
		}
	}

}