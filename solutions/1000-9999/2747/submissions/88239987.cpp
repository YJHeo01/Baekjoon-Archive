#include <iostream>
#include <vector>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	long long int fibo[46];
	fibo[0] = 0;
	fibo[1] = 1;
	for (int i = 2;i <= 45;i++) {
		fibo[i] = fibo[i - 1] + fibo[i - 2];
	}
	int n;
	cin >> n;
	cout << fibo[n];

}