#include <stdio.h>


int main() {
	char gate[100001] = { 0, };
	int answer = 0;
	int airplane;
	int g, p;
	char finish = 1;
	scanf("%d %d", &g, &p);
	for (int i = 0; i < p; i++) {
		scanf("%d", &airplane);
		for (int j = airplane; j >=1; j--)
		{
			if (gate[j] == 0) {
				finish = 0;
				gate[j] = 1;
				answer++;
				break;
			}
		}
		if (finish == 1) {
			break;
		}
		else {
			finish = 1;
		}
	}
	printf("%d", answer);
}