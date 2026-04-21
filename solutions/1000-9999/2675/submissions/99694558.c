//스터디원 코드 확인

#include<stdio.h>
int main() {

	unsigned int R;
	unsigned int A;

	int num = 0;
	int count = 0;


	scanf("%u", &R);

	while (num != R) {
		char s[21] = { 0, };
		scanf("%u", &A);
		scanf(" %s", s);
		while (s[count] != '\0')count++;

		for (int i = 0; i < count; i++) {
			for (int j = 0; j < A; j++) {
				printf("%c", s[i]);
			}
		}
		printf("\n");
		num++;
	}

	return 0;
}