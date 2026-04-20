#include <stdio.h>


int main() {
	char gate[10001] = { 0, };
	int answer = 0;
	int airplane;
	int g, p;
	scanf("%d %d", &g, &p);
	for (int i = 0; i < p; i++) {
		scanf("%d", &airplane);
		if (gate[airplane] == 0) {
			gate[airplane] = 1;
			answer++;
		}
	}
	printf("%d", answer);
}