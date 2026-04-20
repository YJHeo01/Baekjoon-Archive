#include <stdio.h>

int student[20] = { 0, };

void change_value(int left, int right) {
	for (int i = right; i > left; i--) {
		int tmp = student[i];
		student[i] = student[i - 1];
		student[i - 1] = tmp;
	}

}
int check_student(int idx) {
	for (int i = 0; i < idx; i++) {
		if (student[i] > student[idx]) {
			change_value(i, idx);
			return idx - i;
		}
	}
	return 0;
}
int main() {
	int p;
	scanf("%d", &p);
	int answer_array[21] = { 0, };
	for (int j = 0; j < p; j++) {
		int test_num = 0;
		int answer = 0;
		scanf("%d", &test_num);
		for (int i = 0; i < 20; i++) {
			scanf("%d", &student[i]);
			answer += check_student(i);
		}
		answer_array[test_num] = answer;
	}
	for (int i = 1; i <= p; i++) {
		printf("%d %d\n", i, answer_array[i]);
	}
}