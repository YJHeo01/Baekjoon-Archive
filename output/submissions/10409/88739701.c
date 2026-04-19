#include <stdio.h>

int main() {
	int n, t;
	scanf("%d %d", &n, &t);
	int answer = 0;
	for (int i = 0;i < n;i++) {
		int tmp;
		scanf("%d", &tmp);
		t -= tmp;
		if(t < 0) break;
		answer += 1;
	}
	printf("%d", answer);
	return 0;
}