//스터디원 코드 테스트

#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main() {
	 int arr1[100][100];
	 int arr2[100][100];
	 int arr3[100][100];
      int N, M, K;

	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			scanf("%d", &arr1[i][j]);
		}
	}
	scanf("%d %d", &M, &K);
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < K; j++) {
			scanf("%d", &arr2[i][j]);
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			for (int k = 0; k < K; k++) {
				arr3[i][k] += arr1[i][j] * arr2[j][k];
			 }
	    }
	}


	for (int i = 0; i < N; i++) {
		for (int j = 0; j < K; j++) {
			printf("%d ", arr3[i][j]);
		}
		printf("\n");
	}


	return 0;
}