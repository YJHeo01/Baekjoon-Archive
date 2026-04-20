#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
int arr[10000] = { 0, };

int main(int argc, char **argv) {
	int n;
	scanf("%d", &n);
	for (int i = 0;i < n;i++) scanf("%d", &arr[i]);
	sort(arr, arr + n);
	long long int answer = 0;
	answer = arr[0] * arr[1] * arr[2];
	answer = max(answer, arr[0] * arr[1]);
	answer = max(answer, arr[n - 1] * arr[n - 2] * arr[n - 3]);
	answer = max(answer, arr[n - 1] * arr[n - 2]);
	answer = max(answer, arr[n - 1] * arr[0] * arr[1]);
	printf("%lld", answer);
}