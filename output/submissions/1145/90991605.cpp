#include <iostream>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	int arr[5] = { 0, };
	
	for (int i = 0;i < 5;i++) cin >> arr[i];

	for (int val = 1;val <= 1000000; val++) {
		int cnt = 0;
		for (int i = 0;i < 5;i++) {
			if (val % arr[i] == 0) cnt++;
		}
		if (cnt < 3) continue;
		cout << val;
		break;
	}

}