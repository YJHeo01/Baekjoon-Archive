#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;
long long int arr[10000] = { 0, };

int main() {
	int n;
	cin >> n;
	for (int i = 0;i < n;i++) cin >> arr[i];
	sort(arr, arr + n);
	long long int answer = arr[0] * arr[1] * arr[2];
	answer = max(answer, arr[0] * arr[1]);
	answer = max(answer, arr[n - 1] * arr[n - 2] * arr[n - 3]);
	answer = max(answer, arr[n - 1] * arr[n - 2]);
	answer = max(answer, arr[n - 1] * arr[0] * arr[1]);
	printf("%ld", answer);
}