#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

bool compare(int a, int b) {
	return a > b;
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int array[3000] = {0,};
	int n;
	cin >> n;
	for (int i = 0;i < n;i++) {
		for (int j = 0;j < n;j++) {
			cin >> array[n + j];
		}
		sort(array, array + n * 2 + 1, compare);
	}
	cout << array[n - 1];
}