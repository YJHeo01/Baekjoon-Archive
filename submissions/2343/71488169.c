#define MIN(a,b) a > b ? b : a
#define MAX(a,b) a > b ? a : b
#include <stdio.h>
int blue_ray[100000] = { 0, };

int main() {
	int n,m;
	scanf("%d %d", &n, &m);
	int left = 0 ,right = 0;
	for (int i = 0; i < n; i++) {
		scanf("%d", &blue_ray[i]);
		right += blue_ray[i];
		left = MAX(left, blue_ray[i]);
	}
	int answer = right + 1;
	while (left <= right) {
		int mid = (left + right) / 2;
		int cnt = 1;
		int tmp = mid;
		for (int i = 0; i < n; i++) {
			if (blue_ray[i] > tmp) {
				tmp = mid;
				cnt++;
			}
			tmp -= blue_ray[i];
		}
		if (cnt > m) {
			left = mid + 1;
		}
		else
		{
			answer = MIN(answer, mid);
			right = mid - 1;
		}
	}
	printf("%d", answer);

}