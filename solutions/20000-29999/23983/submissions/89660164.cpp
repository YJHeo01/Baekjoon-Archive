#include <iostream>
#include <algorithm>

using namespace std;

long long a[7001] = { 0, };

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL);

	int t;
	cin >> t;

	for (int i = 0;i < t;i++) {
		int n;
		cin >> n;
		for (int j = 0;j < n;j++) {
			cin >> a[j];
		}
		sort(a, a + n);
		int answer = 0;
		for (int x = 1;x < n-1;x++) {
			for (int y = 0;y < x;y++) {
				long long  multiple = a[x] * a[y];
				int left, right, target;
				left = x + 1;
				right = n - 1;
				target = n - 1;
				while (left <= right) {
					int mid = (left + right) / 2;
					if (a[mid] <= multiple) {
						left = mid + 1;
						if(a[mid]==multiple) target = mid;
					}
					else {
						right = mid - 1;
					}
				}
				if (a[target] != multiple) continue;
				answer++;
				answer += target;
				left = x + 1;
				right = target;
				while (left <= right) {
					int mid = (left + right) / 2;
					if (a[mid] < multiple) {
						left = mid + 1;
						
					}
					else {
						right = mid - 1;
						if(a[mid]==multiple) target = mid;
					}
				}
				answer -= target;
			}
		}
		cout << "Case #" << i+1 << ": " << answer << "\n";
	}

}