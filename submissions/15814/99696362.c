#include <stdio.h>

int main() {
	char S[101] = { 0, };
	scanf("%s", S);
	int t;
	scanf("%d", &t);
	for (int i = 0;i < t;i++) {
		int a, b;
		scanf("%d %d", &a, &b);
		char tmp = S[a];
		S[a] = S[b];
		S[b] = tmp;
	}
	printf("%s", S);

	return 0;
}