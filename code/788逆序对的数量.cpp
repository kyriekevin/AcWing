#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

typedef long long LL;

const int N = 1e5 + 10;
int g[N], temp[N];
int n;

LL msort(int s, int e) {
	if (s >= e) return 0;
	int mid = s + e >> 1;
	LL res = msort(s, mid) + msort(mid + 1, e);

	int i = s, j = mid + 1, k = 0;
	while (i <= mid && j <= e) {
		if (g[i] <= g[j])
			temp[k++] = g[i++];
		else {
			res += mid - i + 1;
			temp[k++] = g[j++];
		}
	}

	while (i <= mid) temp[k++] = g[i++];
	while (j <= e) temp[k++] = g[j++];

	for (int i = s; i <= e; i++)
		g[i] = temp[i - s];	

	return res;
}

int main() {
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> g[i];
	
	cout << msort(0, n - 1) << endl;

	return 0;
}
