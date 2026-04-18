#include <iostream>
#include <cmath>

int arr[100000] = { 0, };

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);   
	int n, k;
	cin >> n >> k;
	for (int i = 0;i < n;i++) cin >> arr[i];
	int answer = 1987654321;
	int left = 0;
	int right = 1000000000;
	while (left <= right) {
		int H = (left + right) / 2;
		int cnt = 0;
		for (int x = 0;x < n;x++) {
			int tmp = 0;
			for (int dx = -1;dx <= 1;dx++) {
				int nx = x + dx;
				if (nx < 0 || nx >= n) continue;
				if (abs(arr[nx] - arr[x]) > H) tmp = 1;
			}
			cnt += tmp;
		}
		if (cnt <= k) {
			answer = H;
			right = H - 1;
		}
		else left = H + 1;
	}
	printf("%d", answer);
}