#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

const int N = 1e4 + 10;
int a[N], b[N];
int n;

int main() {
	cin >> n;
	int minv = 0, maxv = 1e9;
	for (int i = 0; i < n; i++) {
		int l = 1, r = 1e9;
		cin >> a[i] >> b[i];

		while (l < r) {
			int mid = l + r >> 1;
			if (a[i] / mid <= b[i]) r = mid;
			else l = mid + 1;
		}
		minv = max(minv, l);

		r = 1e9;
		while (l < r) {
			int mid = l + r + 1 >> 1;
			if (a[i] / mid >= b[i]) l = mid;
			else r = mid - 1;
		}
		maxv = min(maxv, l);
	}

	cout << minv << " " << maxv << endl;

	return 0;
}
