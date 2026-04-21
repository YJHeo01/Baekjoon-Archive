#include <iostream>
#include <cmath>

using namespace std;

int A[300000] = { 0, };

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL);
	
	int n;
	cin >> n;
	
	for (int i = 0;i < n;i++) cin >> A[i];
	
	int answer = 0;
	
	for (int i = 0;i <= 1;i++) {
		int tmp = 0;
		for (int j = 0;j < n;j++) {
			if ((tmp + i) % 2 == A[j] % 2) tmp++;
		}
		answer = max(answer, tmp);
	}

	cout << answer;

}