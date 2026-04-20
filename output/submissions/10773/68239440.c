#include <stdio.h>


int main()
{
	int stack[100001] = { 0 };
	int top = -1;
	int k,tmp;
	scanf("%d", &k);
	int answer = 0;
	for (int i = 0; i < k; i++) {
		scanf("%d", &tmp);
		if (tmp != 0) {
			stack[++top] = tmp;
		}
		else {
			top--;
		}
	}
	for (int i = 0; i <= top; i++) {
		answer += stack[i];
	}
	printf("%d", answer);
}